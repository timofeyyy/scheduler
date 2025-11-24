from sqlalchemy import func
from sqlalchemy.orm import Session
from ..db_oim_orm import Manufacturers
from .family import DataRefFamily


class ManufacturerRepo(DataRefFamily):
    def select(self):
        pass

    def __init__(self, engine):
        self.engine = engine

    def get_obj_by_value(self, value):
        with Session(autoflush=False, bind=self.engine) as db:
            manufacturer: Manufacturers = db.query(Manufacturers).filter(func.lower(Manufacturers.ManufacturerName) == value.lower()).first()
            if manufacturer is None:
                manufacturer = Manufacturers()
                manufacturer.ManufacturerName = value
                db.add(manufacturer)
                db.commit()
                db.refresh(manufacturer)
            db.expunge(manufacturer)
            # print(f"manufacturer.ID = {manufacturer.ID}")
            return manufacturer
