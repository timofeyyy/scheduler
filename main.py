from sqlalchemy.orm import sessionmaker, Session



import launcher
from db.db_connect import get_connection_mssql
from db.db_session import DBSession
from reader.data_reader import Reader
from db.db_oim_orm import Microchips, ComponentTypes, ComponentKinds, Manufacturers
from db.db_connect import get_connection_mssql
from reader import data_reader

launcher.start()
# reader = Reader()
# records = reader.fetch()
# reader.print()
# db = DBSession()
# db.insertRowsFromFile()


# import configparser
#
# config = configparser.ConfigParser()
# config.read("settings.ini")
#
# print(config["dir"]["microparser"])
# 'johndoe'