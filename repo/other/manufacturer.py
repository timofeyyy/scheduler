from sqlalchemy.orm import Session
from db import ComponentTypes, Manufacturers
from .family import ComponentReferenceFamily


class ManufacturerRepo(ComponentReferenceFamily):

    def __init__(self, engine):
        self.engine = engine

    def get_id_by_value(self, name):
        with Session(autoflush=False, bind=self.engine) as db:
            manufacturer = db.query(Manufacturers).filter(Manufacturers.ManufacturerName == name).first()
            if manufacturer is None:
                manufacturer = Manufacturers()
                manufacturer.ManufacturerName = name
                db.add(manufacturer)
                db.commit()
            return manufacturer.ID
