import urllib
from typing import Generator
from contextlib import contextmanager
from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import OperationalError, DBAPIError
from config.settings import DB_SERVER, DB_USERNAME, DB_PASSWORD

import urllib.parse
from typing import Optional, Any
from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine, Connection
from sqlalchemy.exc import SQLAlchemyError


class SQLServerConnection:
    """
    Manages SQLAlchemy engine creation and provides context manager 
    support for connecting to SQL Server.
    """

    def __init__(
        self,
        server: str = "localhost",
        database: str = "BookTrackerDB",
        username: Optional[str] = None,
        password: Optional[str] = None,
        driver: str = "ODBC Driver 17 for SQL Server",
        trusted_connection: bool = False,
    ):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.driver = driver
        self.trusted_connection = trusted_connection
        self._engine: Optional[Engine] = None
        self._connection: Optional[Connection] = None

    def _build_connection_string(self) -> str:
        """Constructs the ODBC connection string for SQLAlchemy."""
        conn_parts = [
            f"DRIVER={{{self.driver}}}",
            f"SERVER={self.server}",
            f"DATABASE={self.database}",
            "TrustServerCertificate=yes",
        ]

        if self.trusted_connection:
            conn_parts.append("Trusted_Connection=yes")
        elif self.username and self.password:
            conn_parts.extend([f"UID={self.username}", f"PWD={self.password}"])
        else:
            raise ValueError(
                "Must specify either (username and password) OR set trusted_connection=True"
            )

        odbc_str = ";".join(conn_parts) + ";"
        params = urllib.parse.quote_plus(odbc_str)
        return f"mssql+pyodbc:///?odbc_connect={params}"

    @property
    def engine(self) -> Engine:
        """Lazily creates and returns the SQLAlchemy Engine."""
        if self._engine is None:
            connection_url = self._build_connection_string()
            self._engine = create_engine(connection_url, pool_pre_ping=True)
        return self._engine

    # --- Context Manager Protocol ---

    def __enter__(self) -> Connection:
        """
        Enters the context block. Establishes and returns an active 
        SQLAlchemy Connection object.
        """
        self._connection = self.engine.connect()
        return self._connection

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """
        Exits the context block. Commits the transaction if successful,
        rolls back if an exception occurred, and closes the connection.
        """
        if self._connection:
            try:
                if exc_type is not None:
                    # An error occurred inside the 'with' block; roll back changes
                    self._connection.rollback()
                    print(f"❌ Transaction rolled back due to error: {exc_val}")
                else:
                    # Transaction succeeded; commit changes
                    self._connection.commit()
            finally:
                self._connection.close()
                self._connection = None

    # --- Helper Methods ---

    def test_connection(self) -> bool:
        """Tests if the SQL Server database is reachable."""
        try:
            with self as conn:
                result = conn.execute(
                    text("SELECT @@VERSION AS version, DB_NAME() AS db_name;")
                ).fetchone()

                print("✅ Connection Successful!")
                print(f"   Database: {result.db_name}")
                print(f"   SQL Server Version: {result.version.splitlines()[0]}")
                return True

        except SQLAlchemyError as e:
            print(f"❌ Connection Failed! Error: {e}")
            return False


# class SQLServerConnection:
    """
    Database connection manager class for Microsoft SQL Server using SQLAlchemy and pyodbc.
    """
    def __init__(
        self,
        server: str = DB_SERVER,
        database: str = 'BuzzliveWarehouse',
        username: str = DB_USERNAME,
        password: str = DB_PASSWORD,
        driver: str = "ODBC Driver 18 for SQL Server",
        port: int = 1433,
        trusted_connection: bool = False,
        trust_server_certificate: str = "yes",
        fast_executemany: bool = True,
        ):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.driver = driver
        self.port = port
        self.trusted_connection = trusted_connection
        self.trust_server_certificate = trust_server_certificate
        self.fast_executemany = fast_executemany

        self.engine: Engine = self._create_engine()
        self.SessionLocal = sessionmaker(bind=self.engine, autoflush=False, autocommit=False)

    def _build_connection_string(self) -> str:
        """Builds a formatted ODBC connection URL for SQLAlchemy."""
        params = f"DRIVER={{{self.driver}}};SERVER={self.server},{self.port};DATABASE={self.database};"

        if self.trusted_connection:
            params += "Trusted_Connection=yes;"
        else:
            params += f"UID={self.username};PWD={self.password};"

        # ODBC Driver 18 requires SSL settings configuration
        if "18" in self.driver and self.trust_server_certificate:
            params += "TrustServerCertificate=yes;"

        # URL encode raw connection parameters to safely handle special characters in passwords
        encoded_params = urllib.parse.quote_plus(params)
        return f"mssql+pyodbc:///?odbc_connect={encoded_params}"

    def _create_engine(self) -> Engine:
        """Initializes the SQLAlchemy Engine."""
        connection_url = self._build_connection_string()
        return create_engine(
            connection_url,
            fast_executemany=self.fast_executemany,  # Speeds up batch inserts with pandas/SQLAlchemy
            pool_pre_ping=True,                     # Verifies connection health before usage
            pool_size=10,
            max_overflow=20,
        )
    def test_connection(self) -> bool:
        """
        Tests the database connection by executing a lightweight query.
        Returns True if successful, raises/prints an error if failed.
        """
        try:
            with self.get_connection() as conn:
                # Execute a simple lightweight query
                result = conn.execute(text("SELECT 1;")).scalar()
                if result == 1:
                    print("✅ Database connection successful!")
                    return True
        except (OperationalError, DBAPIError) as e:
            print(f"❌ Connection failed: {e}")
            return False
        except Exception as e:
            print(f"❌ Unexpected error during connection test: {e}")
            return False

    @contextmanager
    def get_session(self) -> Generator[Session, None, None]:
        """
        Context manager for handling SQLAlchemy ORM Sessions safely.
        Automatically handles commit, rollback, and closing.
        """
        session: Session = self.SessionLocal()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    @contextmanager
    def get_connection(self):
        """Context manager for raw SQLAlchemy Core connections."""
        connection = self.engine.connect()
        try:
            yield connection
        finally:
            connection.close()

    def dispose(self):
        """Closes all underlying connection pools."""
        self.engine.dispose()