import configparser
import os

from sqlalchemy import create_engine
# from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.engine import URL
from sqlalchemy_utils import database_exists, create_database

from .db_oim_orm import create_tables


def get_connection_mssql():
    config = configparser.ConfigParser()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    settings_path = os.path.join(base_dir, "..", "settings.ini")
    config.read(settings_path, encoding='utf-8')
    connection_string = config['db']['connectionString']
    connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
    engine = create_engine(connection_url)

    if not database_exists(engine.url):
        create_database(engine.url)
        print(f"created new database")
        create_tables(engine)
    return engine


