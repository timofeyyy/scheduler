from datetime import date

from scheduler.reader import PDFStorage
from .family import ComponentBase, ComponentFamilyBase, make_dictionary, compare_rows
from scheduler.settings import get_settings
from ..db_oim_orm import Resistors


class ResistorsRepo(ComponentBase, ComponentFamilyBase):
    __typename__ = Resistors.__typename__

    def select_all_wrap(self):
        return self.select_all(table=Resistors)

    def __init__(self, engine):
        super().__init__(engine)
        self.engine = engine

    # шаблонный метод можно сделать позже

    def insert_many(self, rows):
        print(self.__typename__)
        all_rows = self.select_all_wrap()
        rows_dict = make_dictionary(all_rows)
        for row in rows:
            existing_rows = rows_dict.get(row.ComponentName)
            if existing_rows is not None and compare_rows(row=row, existing_rows=existing_rows, component_type=Resistors):
                continue
            component_type = self.type.get_obj_by_en_value(self.__typename__)
            setattr(row, "Type_ID", component_type.ID)
            manufacturer_id = self.manufacturer.get_obj_by_value(getattr(row, "ManufacturerName")).ID
            setattr(row, "ManufacturerName_ID", manufacturer_id)
            kind_id = self.kind.get_obj_by_ru_value("Резисторы маломощные").ID
            setattr(row, "Kind_ID", kind_id)
            name = self.pdf.download(link=getattr(row, "SpecificationDoc"), catalog=component_type.EnComponentType)
            setattr(row, "SpecificationDoc", name)
            setattr(row, "Insertion", date.today())
            self.insert_one(row)

    # def select_all(self):
    #     with Session(autoflush=False, bind=self.engine) as db:
    #         return db.query(Resistors).all()



