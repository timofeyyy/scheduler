import configparser

from db.db_connect import get_connection_mssql
from db import Resistors, Microchips
from reader import data_reader
from repo import ResistorsRepo, MicrochipsRepo
import repo
class UnitOfWork:
    def __init__(self):
        self.engine = get_connection_mssql()
        config = configparser.ConfigParser()
        config.read("settings.ini")
        self._resistors = None
        self._microchips = None
        self.component = {
            Resistors.__tablename__: self.resistors,
            Microchips.__tablename__: self._microchips
        }

    @property
    def resistors(self):
        if self._resistors is None:
            self._resistors = ResistorsRepo(self.engine)
        return self._resistors

    @property
    def microchips(self):
        if self._microchips is None:
            self._microchips = MicrochipsRepo(self.engine)
        return self._microchips

    def get_repo(self, table_name):
        return self.component.get(table_name)

    def insert_many(self, table_name):
        rep = getattr(repo, f"{table_name}Repo")(engine=self.engine)
        reader = data_reader.Reader()
        rows = reader.fetch(table_name)
        rep.insert_many(rows=rows)
