from sqlalchemy.orm import Session

from scheduler.db import *
from scheduler.reader import PDFStorage
from .family import ComponentBaseMicrochips, make_dictionary, compare_rows, ComponentFamilyBase
from scheduler.settings import get_settings
from ..db_oim_orm import Microchips
from datetime import date

class MicrochipsRepo(ComponentBaseMicrochips, ComponentFamilyBase):
    __typename__ = Microchips.__typename__

    def select_all_wrap(self):
        return self.select_all(table=Microchips)

    def __init__(self, engine):
        super().__init__(engine)
        self.engine = engine

    def insert_many(self, rows):
        print(self.__typename__)
        all_rows = self.select_all_wrap()
        rows_dict = make_dictionary(all_rows)
        for row in rows:
            existing_rows = rows_dict.get(row.ComponentName)
            if existing_rows is not None and compare_rows(row=row, existing_rows=existing_rows, component_type=Microchips):
                continue
            component_type = self.type.get_obj_by_en_value(self.__typename__)
            setattr(row, "Type_ID", component_type.ID)
            manufacturer_id = self.manufacturer.get_obj_by_value(getattr(row, "ManufacturerName")).ID
            setattr(row, "ManufacturerName_ID", manufacturer_id)
            kind_id = self.kind.get_obj_by_ru_value("микросхема памяти").ID
            setattr(row, "Kind_ID", kind_id)
            technology_id = self.technology.get_obj_by_ru_value("не указано").ID
            setattr(row, "TechnologyName_ID", technology_id)
            name = self.pdf.download(link=getattr(row, "SpecificationDoc"), catalog=component_type.EnComponentType)
            setattr(row, "SpecificationDoc", name)
            setattr(row, "Insertion", date.today())
            self.insert_one(row)

    # def select_all(self):
    #     with Session(autoflush=False, bind=self.engine) as db:
    #         return db.query(Microchips).all()
