from abc import *

from sqlalchemy.orm import Session

from scheduler.db.repo.data_ref.component_type import ComponentTypeRepo
from scheduler.db.repo.data_ref.manufacturer import ManufacturerRepo
from scheduler.db.repo.data_ref.technology import TechnologyRepo
from scheduler.db.repo.data_ref.component_kind import ComponentKindRepo
from sqlalchemy.inspection import inspect

from scheduler.reader import PDFStorage
from scheduler.settings import get_settings


class ComponentFamilyBase(ABC):
    @abstractmethod
    def select_all_wrap(self): pass
    @abstractmethod
    def insert_many(self, rows): pass


class ComponentBase(ABC):

    def __init__(self, connection):
        self.engine = connection
        self._type = None
        self._manufacturer = None
        self._technology = None
        self._kind = None
        self.pdf = PDFStorage()

    @property
    def type(self):
        if self._type is None:
            self._type = ComponentTypeRepo(self.engine)
        return self._type

    @property
    def manufacturer(self):
        if self._manufacturer is None:
            self._manufacturer = ManufacturerRepo(self.engine)
        return self._manufacturer

    @property
    def kind(self):
        if self._kind is None:
            self._kind = ComponentKindRepo(self.engine)
        return self._kind

    def select_all(self, table):
        with Session(autoflush=False, bind=self.engine) as db:
            return db.query(table).all()

    # @property
    # def technology(self):
    #     if self._technology is None:
    #         self._technology = TechnologyRepo(self.engine)
    #     return self._technology

    def insert_one(self, row):
        with Session(autoflush=False, bind=self.engine) as db:
            print(f"inserted row {vars(row)}")
            db.add(row)
            db.commit()


def compare_rows(row, existing_rows, component_type):
    mapper = inspect(component_type)
    for existing_row in existing_rows:
        satisfy_count = 0
        actual_mapper_len = 0
        for attr in mapper.attrs:
            if getattr(attr, "columns", None) and attr.columns[0].info.get("compare"):
                actual_mapper_len += 1
                existing_value = getattr(existing_row, attr.key, None)
                row_value = getattr(row, attr.key, None)
                if existing_value is not None:
                    existing_value = f"{existing_value}"
                if row_value == existing_value:
                    satisfy_count += 1
        if satisfy_count == actual_mapper_len:
            return True
    return False


def make_dictionary(rows):
    rows_dict = {}
    for row in rows:
        if rows_dict.get(row.ComponentName) is None:
            rows_dict[row.ComponentName] = []
        rows_dict[row.ComponentName].append(row)
    return rows_dict


class ComponentBaseMicrochips(ComponentBase):

    def __init__(self, connection):
        super().__init__(connection=connection)
        self.engine = connection
        self._technology = None

    @property
    def technology(self):
        if self._technology is None:
            self._technology = TechnologyRepo(self.engine)
        return self._technology
