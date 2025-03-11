from sqlalchemy.orm import sessionmaker, Session
from db.db_connect import get_connection_mssql
from reader.data_reader import Reader
from db.db_oim_orm import Microchips, ComponentTypes, ComponentKinds, Manufacturers
from db.db_connect import get_connection_mssql
from reader import data_reader
from scheduler.db.db_session import DBSession

# launcher.start()
# reader = Reader()
# records = reader.fetch()
# reader.print()

#Microchip{id=null, docId=null, componentName='23K256-I/SN', componentType='Диод', componentKind='флеш-память', manufacturer='ОАО ИНТЕГРАЛ', interfaceName='spi', voltageMin=2.7, voltageMax=3.6, frequency=20.0, bitDepth=null, consumptionCurrent=null, technology=1, temperatureMin=-40.0, temperatureMax=85.0, radiationResistance=null, radiationResistanceMeasures='null', memoryFormat='SRAM', samplingTime=null, packageType='SOIC-8(3.90мм)', qualification='null', remark1='null'}


# engine = get_connection_mssql()
db = DBSession()
db.insertRowsFromFile()
# componentTypeId = db.getComponentTypeIdByName("ДиОд")
# print(componentTypeId)
# componentKindId = db.getComponentKindIdByName("флеш-память")
# print(componentKindId)
# manufacturerId = db.getManufacturerIdByName("ОАО ИНТЕГРАЛ")
# print(manufacturerId)

# with Session(autoflush=False, bind=get_connection_mssql()) as db:
#     kind = db.query(db_oim_orm.ComponentKinds).all()
#
#     print(f'{kind.ID} {kind.RuComponentType}')
# Session = sessionmaker(autoflush=False, bind=engine)
# for record in records:
#     with Session(autoflush=False, bind=engine) as db:
#         db.add(record)
#         db.commit()

# with Session(autoflush=False, bind=get_connection_mssql()) as db:
#     kinds = db.query(ComponentKinds).all()
#     for kind in kinds:
#         print(kind.RuComponentKind)

# with Session(autoflush=False, bind=get_connection_mssql()) as db:
#     kinds = db.query(Manufacturers).all()
#     for kind in kinds:
#         print(kind.ManufacturerName)
#





