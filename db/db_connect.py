from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from scheduler.settings import get_settings


def get_connection_mssql():
    config = get_settings()
    connection_string = config['db']['connectionString']
    # print(connection_string)
    connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
    engine = create_engine(connection_url)
    return engine


