import configparser
import string

from sqlalchemy.orm import sessionmaker, Session

from reader.pdf_parser import PDFParser
# from .db_oim_orm import ComponentTypes
from .db_connect import get_connection_mssql
from .db_oim_orm import ComponentTypes, ComponentKinds, Manufacturers, Technologies
from reader import data_reader




class DBSession:
    def __init__(self):
        self.engine = get_connection_mssql()
        config = configparser.ConfigParser()
        config.read("settings.ini")
        self.pdf = PDFParser(config['pdf']['storeDir'])


    def getComponentTypeIdByName(self, name):
        with Session(autoflush=False, bind=self.engine) as db:
            type = db.query(ComponentTypes).filter(ComponentTypes.RuComponentType == name).first()
            if type == None:
                type = ComponentTypes()
                type.RuComponentType = name
                # type.EnComponentType = name
                db.add(type)
                db.commit()
            # print(f'{type.ID} {type.RuComponentType}')
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
            # print(f'{kind.ID} {kind.RuComponentKind}')
            return kind.ID

    def getManufacturerIdByName(self, name):
        with Session(autoflush=False, bind=self.engine) as db:
            manufacturer = db.query(Manufacturers).filter(Manufacturers.ManufacturerName == name).first()
            if manufacturer == None:
                manufacturer = Manufacturers()
                manufacturer.ManufacturerName = name
                db.add(manufacturer)
                db.commit()
            # print(f'{manufacturer.ID} {manufacturer.ManufacturerName}')
            return manufacturer.ID

    def getTechnologyIdByName(self, name):
        with Session(autoflush=False, bind=self.engine) as db:
            technology = db.query(Technologies).filter(Technologies.RuTechnologyName == name).first()
            if technology == None:
                technology = Technologies()
                technology.RuTechnologyName = name
                db.add(technology)
                db.commit()
            # print(f'{technology.ID} {technology.RuTechnologyName}')
            return technology.ID


    def insertRowsFromFile(self, tableName):
        reader = data_reader.Reader()
        records = reader.fetch(tableName)
        delegateName = reader.getFncName(tableName)
        if delegateName and records:
            print(delegateName)
            reader.print()
            call = getattr(self, delegateName)
            call(records)


    def sendMicrochips(self, records):
        print("sendMicrochips")
        for record in records:
            with Session(autoflush=False, bind=self.engine) as db:
                componentName = getattr(record, "ComponentName")
                # print(componentName)
                componentNameRec = db.query(type(record)).filter(type(record).ComponentName == componentName).first()
                # print(componentNameRec)
                if(componentNameRec == None):
                    manufacturer = getattr(record, "ManufacturerName")
                    manufacturerId = self.getManufacturerIdByName("ОАО ИНТЕГРАЛ")
                    setattr(record, "ManufacturerName_ID", manufacturerId)

                    # ctype = getattr(record, "Type")
                    ctypeId = self.getComponentTypeIdByName("микросхема")
                    setattr(record, "Type_ID", ctypeId)

                    # kind = getattr(record, "Kind")
                    kindId = self.getComponentKindIdByName("флеш-память")
                    setattr(record, "Kind_ID", kindId)

                    # technology = getattr(record, "TechnologyName")
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

                    name = self.pdf.download(getattr(record, "Remark1"))
                    setattr(record, "Remark1", name)

                    # db.add(record)
                    # db.commit()

    def sendResistors(self, records):
        print("sendResistors")
        for record in records:
            with Session(autoflush=False, bind=self.engine) as db:
                componentName = getattr(record, "ComponentName")
                # print(componentName)
                componentNameRec = db.query(type(record)).filter(type(record).ComponentName == componentName).first()
                # print(componentNameRec)
                if(componentNameRec == None):
                    manufacturerId = self.getManufacturerIdByName("Taiwan")
                    setattr(record, "ManufacturerName_ID", manufacturerId)

                    ctypeId = self.getComponentTypeIdByName("резистор")
                    setattr(record, "Type_ID", ctypeId)
                    # print(f"${getattr(record, "Remark1")} ready")
                    name = self.pdf.download(getattr(record, "Remark1"))
                    setattr(record, "Remark1", name)
                    print(f"${name} downloaded")
                    db.add(record)
                    db.commit()