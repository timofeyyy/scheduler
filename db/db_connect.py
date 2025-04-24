from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.engine import URL

from .db_oim_orm import create_tables


def get_connection_mssql():
    connection_string = ("Driver={ODBC Driver 18 for SQL Server};Server=tcp:127.0.0.1,1433;Database=ComponentDB;Uid=HP;Pwd=g@!$V203Wz7JRqK*&Za!8HN2$C!Q8myWHh%ZNYB53r1K&r&5I8;Encrypt=yes;TrustServerCertificate=yes;Connection Timeout=10;")
    connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})

    engine = create_engine(connection_url)

    if not database_exists(engine.url):
        create_database(engine.url)
        print(f"created new database")
        create_tables(engine)
    return engine

