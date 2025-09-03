import configparser
from sqlalchemy.orm import Session
from db import Resistors
from reader import PDFParser
from .family import ComponentFamily


class ResistorsRepo(ComponentFamily):
    def __init__(self, engine):
        super().__init__(engine)
        config = configparser.ConfigParser()
        config.read("settings.ini")
        self.engine = engine
        self.pdf = PDFParser(config['pdf']['storeDir'])

    # шаблонный метод можно сделать позже

    def insert_many(self, rows):
        print("resistors")
        all_rows = self.select_all()
        rows_dict = self.get_dictionary_from_rows(all_rows)
        for row in rows:
            existing_rows = rows_dict.get(row.ComponentName)
            if existing_rows is not None and self.compare_rows(row=row, existing_rows=existing_rows, component_type=Resistors):
                continue
            type_id = self.type.get_id_by_value("резистор")
            setattr(row, "Type_ID", type_id)
            manufacturer_id = self.manufacturer.get_id_by_value("Taiwan")
            setattr(row, "ManufacturerName_ID", manufacturer_id)
            manufacturer_id = self.kind.get_id_by_value("не указано")
            setattr(row, "Kind_ID", manufacturer_id)
            name = self.pdf.download(getattr(row, "Remark1"))
            setattr(row, "Remark1", name)
            self.insert_one(row)

    def select_all(self):
        with Session(autoflush=False, bind=self.engine) as db:
            return db.query(Resistors).all()



