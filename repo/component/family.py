from abc import *

from sqlalchemy.orm import Session

from repo.other.component_type import ComponentTypeRepo
from repo.other.manufacturer import ManufacturerRepo
from repo.other.technology import TechnologyRepo
from repo.other.component_kind import ComponentKindRepo
from sqlalchemy.inspection import inspect


class ComponentFamily(ABC):

    def __init__(self, connection):
        self.engine = connection
        self._type = None
        self._manufacturer = None
        self._technology = None
        self._kind = None

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

    @property
    def technology(self):
        if self._technology is None:
            self._technology = TechnologyRepo(self.engine)
        return self._technology

    def compare_rows(self, row, existing_rows, component_type):
        mapper = inspect(component_type)
        for existing_row in existing_rows:
            satisfy_count = 0
            actual_mapper_len = 0
            for attr in mapper.attrs:
                if getattr(attr, "columns", None) and attr.columns[0].info.get("skip") is None:
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

    def insert_one(self, row):
        with Session(autoflush=False, bind=self.engine) as db:
            print(f"inserted row {vars(row)}")
            db.add(row)
            db.commit()

    def get_dictionary_from_rows(self, rows):
        rows_dict = {}
        for row in rows:
            if rows_dict.get(row.ComponentName) is None:
                rows_dict[row.ComponentName] = []
            rows_dict[row.ComponentName].append(row)
        return rows_dict
