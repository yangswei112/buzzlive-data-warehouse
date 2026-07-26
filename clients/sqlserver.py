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
        port: int | None = None,  # Set to None by default so SQLEXPRESS isn't forced onto 1433
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
        """Builds a formatted ODBC connection URL for SQLAlchemy matching the working standalone format."""
        # Include port only if explicitly provided (e.g., standard SQL Server instances)
        server_str = f"{self.server},{self.port}" if self.port else self.server

        # Wrap driver name in curly braces as required by pyodbc ODBC specs
        params = f"DRIVER={{{self.driver}}};SERVER={server_str};DATABASE={self.database};"

        if self.trusted_connection:
            params += "Trusted_Connection=yes;"
        else:
            params += f"UID={self.username};PWD={self.password};"

        if self.trust_server_certificate:
            params += "TrustServerCertificate=yes;"

        encoded_params = urllib.parse.quote_plus(params)
        return f"mssql+pyodbc:///?odbc_connect={encoded_params}"

    def _create_engine(self) -> Engine:
        """Initializes the SQLAlchemy Engine."""
        connection_url = self._build_connection_string()
        return create_engine(
            connection_url,
            fast_executemany=self.fast_executemany,
            pool_pre_ping=True,
            pool_size=10,
            max_overflow=20,
        )

    @contextmanager
    def get_session(self) -> Generator[Session, None, None]:
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
        with self.engine.connect() as connection:
            yield connection

    def dispose(self):
        self.engine.dispose()

    def test_connection(self) -> bool:
        try:
            with self.get_connection() as conn:
                result = conn.execute(text("SELECT @@VERSION;")).scalar()
                print("✅ Database connection successful!")
                print(f"Connected to Version:\n{result}")
                return True
        except (OperationalError, DBAPIError) as e:
            print(f"❌ Connection failed: {e}")
            return False
        except Exception as e:
            print(f"❌ Unexpected error during connection test: {e}")
            return False