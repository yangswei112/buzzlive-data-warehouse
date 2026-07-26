import urllib.parse
from typing import Generator
from contextlib import contextmanager

from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import OperationalError, DBAPIError


class SQLServerConnection:
    """
    Database connection manager class for Microsoft SQL Server using SQLAlchemy and pyodbc.
    """

    def __init__(
        self,
        server: str,
        database: str,
        username: str | None = None,
        password: str | None = None,
        driver: str = "ODBC Driver 18 for SQL Server",
        port: int = 1433,
        trusted_connection: bool = False,
        trust_server_certificate: bool = True,
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
        params = f"DRIVER={self.driver};SERVER={self.server},{self.port};DATABASE={self.database};"

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
        with self.engine.connect() as connection:
            yield connection

    def dispose(self):
        """Closes all underlying connection pools."""
        self.engine.dispose()

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
                return False
        except (OperationalError, DBAPIError) as e:
            print(f"❌ Connection failed: {e}")
            return False
        except Exception as e:
            print(f"❌ Unexpected error during connection test: {e}")
            return False