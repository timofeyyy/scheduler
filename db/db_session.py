import string

from sqlalchemy.orm import sessionmaker, Session
# from .db_oim_orm import ComponentTypes
from .db_connect import get_connection_mssql
from .db_oim_orm import ComponentTypes, ComponentKinds, Manufacturers
from scheduler.reader import data_reader




class DBSession:
    def __init__(self):
        self.engine = get_connection_mssql()

    def getComponentTypeIdByName(self, name):
        with Session(autoflush=False, bind=self.engine) as db:
            type = db.query(ComponentTypes).filter(ComponentTypes.RuComponentType == name).first()
            if type == None:
                type = ComponentTypes()
                type.RuComponentType = name
                type.EnComponentType = name
                db.add(type)
                db.commit()
            print(f'{type.ID} {type.RuComponentType}')
            return type.ID

    def getComponentKindIdByName(self, name):
        with Session(autoflush=False, bind=self.engine) as db:
            kind = db.query(ComponentKinds).filter(ComponentKinds.RuComponentKind == name).first()
            if kind == None:
                kind = ComponentKinds()
                kind.RuComponentKind = name
                kind.EnComponentKind = name
                db.add(kind)
                db.commit()
            print(f'{kind.ID} {kind.RuComponentKind}')
            return kind.ID

    def getManufacturerIdByName(self, name):
        with Session(autoflush=False, bind=self.engine) as db:
            manufacturer = db.query(Manufacturers).filter(Manufacturers.ManufacturerName == name).first()
            if manufacturer == None:
                manufacturer = Manufacturers()
                manufacturer.ManufacturerName = name
                db.add(manufacturer)
                db.commit()
            print(f'{manufacturer.ID} {manufacturer.ManufacturerName}')
            return manufacturer.ID

    def insertRowsFromFile(self):

        reader = data_reader.Reader()
        records = reader.fetch()
        reader.print()
        # print(len(records))
        for record in records:
            with Session(autoflush=False, bind=self.engine) as db:
                componentName = getattr(record, "ComponentName")
                print(componentName)
                componentNameRec = db.query(type(record)).filter(type(record).ComponentName == componentName).first()
                print(componentNameRec)
                if(componentNameRec == None):
                    manufacturer = getattr(record, "ManufacturerName")
                    manufacturerId = self.getManufacturerIdByName(manufacturer)
                    setattr(record, "ManufacturerName_ID", manufacturerId)

                    ctype = getattr(record, "Type")
                    ctypeId = self.getComponentTypeIdByName(ctype)
                    setattr(record, "Type_ID", ctypeId)

                    kind = getattr(record, "Kind")
                    kindId = self.getComponentKindIdByName(kind)
                    setattr(record, "Kind_ID", kindId)

                    print(f'{kindId} {ctypeId} {manufacturerId}')

                    db.add(record)
                    db.commit()

        # reader.clear()