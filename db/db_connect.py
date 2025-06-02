import configparser

from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.engine import URL

from .db_oim_orm import create_tables


def get_connection_mssql():
    config = configparser.ConfigParser()
    config.read("settings.ini")
    print(config['db']['connectionString'])
    connection_string = (
        r"Driver={ODBC Driver 18 for SQL Server};Server=tcp:127.0.0.1,1433;Database=ComponentDB;Uid=Тимофей;"
        r"Pwd=BqCPEE&82I!Aar#9c1QX45$&3E5p!!L0eX6LV*9i3SQ!X!5I&6;"
        r"Encrypt=yes;TrustServerCertificate=yes;Connection Timeout=30;"
    )
    connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
    engine = create_engine(connection_url)

    if not database_exists(engine.url):
        create_database(engine.url)
        print(f"created new database")
        create_tables(engine)
    return engine

