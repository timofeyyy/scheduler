from sqlalchemy.orm import sessionmaker, Session

from reader import data_reader
from .db_connect import get_connection_mssql
from .db_oim_orm import ComponentTypes, ComponentKinds, Manufacturers, Technologies





class DBSession:
    def __init__(self):
        self.engine = get_connection_mssql()

    def getComponentTypeIdByName(self, name):
        with Session(autoflush=False, bind=self.engine) as db:
            type = db.query(ComponentTypes).filter(ComponentTypes.RuComponentType == name).first()
            if type == None:
                type = ComponentTypes()
                type.RuComponentType = name
                # type.EnComponentType = name
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
                # kind.EnComponentKind = name
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

    def getTechnologyIdByName(self, name):
        with Session(autoflush=False, bind=self.engine) as db:
            technology = db.query(Technologies).filter(Technologies.RuTechnologyName == name).first()
            if technology == None:
                technology = Technologies()
                technology.RuTechnologyName = name
                db.add(technology)
                db.commit()
            print(f'{technology.ID} {technology.RuTechnologyName}')
            return technology.ID


    def insertRowsFromFile(self):

        reader = data_reader.Reader(
            "D:\\work\\scheduler\\scheduler\\src\\item_properties.json",
            "D:\\work\\scheduler\\scheduler\\src\\componentsFile6.txt"
        )
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
                    manufacturerId = self.getManufacturerIdByName("ОАО ИНТЕГРАЛ")
                    setattr(record, "ManufacturerName_ID", manufacturerId)

                    ctype = getattr(record, "Type")
                    ctypeId = self.getComponentTypeIdByName("микросхема")
                    setattr(record, "Type_ID", ctypeId)

                    kind = getattr(record, "Kind")
                    kindId = self.getComponentKindIdByName("флеш-память")
                    setattr(record, "Kind_ID", kindId)

                    technology = getattr(record, "TechnologyName")
                    technologyId = self.getTechnologyIdByName("cтатическая память с произвольным доступом")
                    setattr(record, "TechnologyName_ID", technologyId)

                    if getattr(record, "MinVoltage") == None:
                        setattr(record, "MinVoltage", 0)
                    if getattr(record, "MaxVoltage") == None:
                        setattr(record, "MaxVoltage", 0)
                    if getattr(record, "MinOperatingTemperature") == None:
                        setattr(record, "MinOperatingTemperature", 0)
                    if getattr(record, "MaxOperatingTemperature") == None:
                        setattr(record, "MaxOperatingTemperature", 0)

                    print(f'{kindId} {ctypeId} {manufacturerId}')

                    db.add(record)
                    db.commit()

        # reader.clear()