from .repo.db_oim_orm import Resistors, Microchips, Capacitors, Diods, Transistors
from .db_connect import get_connection_mssql
from scheduler.reader import Reader
from .repo import ResistorsRepo, MicrochipsRepo, CapacitorsRepo, DiodsRepo, TransistorsRepo


class UnitOfWork:

    def __init__(self):
        self.engine = get_connection_mssql()
        self.__resistors__ = None
        self.__microchips__ = None
        self.__capacitors__ = None
        self.__diods__ = None
        self.__transistors__ = None
        self.component = {
            Resistors.__tablename__: self.resistors,
            Microchips.__tablename__: self.microchips,
            Capacitors.__tablename__: self.capacitors,
            Diods.__tablename__: self.diods,
            Transistors.__tablename__: self.transistors
        }
        self.reader = Reader()

    @property
    def resistors(self):
        if self.__resistors__ is None:
            self.__resistors__ = ResistorsRepo(self.engine)
        return self.__resistors__

    @property
    def microchips(self):
        if self.__microchips__ is None:
            self.__microchips__ = MicrochipsRepo(self.engine)
        return self.__microchips__

    @property
    def capacitors(self):
        if self.__capacitors__ is None:
            self.__capacitors__ = CapacitorsRepo(self.engine)
        return self.__capacitors__

    @property
    def diods(self):
        if self.__diods__ is None:
            self.__diods__ = DiodsRepo(self.engine)
        return self.__diods__

    @property
    def transistors(self):
        if self.__transistors__ is None:
            self.__transistors__ = TransistorsRepo(self.engine)
        return self.__transistors__

    def get_repo(self, table_name):
        return self.component.get(table_name)

    def insert_many(self, table_name):
        rep = self.get_repo(table_name=table_name)
        rows = self.reader.fetch(table_name)
        print(len(rows))
        rep.insert_many(rows=rows)
