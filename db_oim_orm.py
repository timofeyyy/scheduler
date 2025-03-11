from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import NVARCHAR, BIGINT, FLOAT, DOUBLE


Base = declarative_base()


class Manufacturers(Base):
    __tablename__ = 'Manufacturers'

    ID = Column(Integer(), primary_key=True)
    ManufacturerName = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)

    Capacitors = relationship('Capacitors', backref='Manufacturers')
    Resistors = relationship('Resistors', backref='Manufacturers')
    Diods = relationship('Diods', backref='Manufacturers')
    Microchips = relationship('Microchips', backref='Manufacturers')
    Transistors = relationship('Transistors', backref='Manufacturers')
    column_num = 2
    column_names = ('ID', 'ManufacturerName')

    def get_items_tuple(self):
        res = []
        res.extend([self.ID, self.ManufacturerName])
        return tuple(res)


class ComponentKinds(Base):
    __tablename__ = 'ComponentKinds'

    ID = Column(Integer(), primary_key=True)
    RuComponentKind = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)
    EnComponentKind = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)
    Capacitors = relationship('Capacitors', backref='ComponentKinds')
    column_num = 3
    column_names = ('ID', 'RuComponentKind', 'EnComponentKind')

    def get_items_tuple(self):
        res = []
        res.extend([self.ID, self.RuComponentKind, self.EnComponentKind])
        return tuple(res)


class ComponentTypes(Base):
    __tablename__ = 'ComponentTypes'

    ID = Column(Integer(), primary_key=True)
    RuComponentType = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)
    EnComponentType = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)
    Capacitors = relationship('Capacitors', backref='ComponentTypes')
    column_num = 3
    column_names = ('ID', 'RuComponentType', 'EnComponentType')

    def get_items_tuple(self):
        res = []
        res.extend([self.ID, self.RuComponentType, self.EnComponentType])
        return tuple(res)


class Technologies(Base):
    __tablename__ = 'Technologies'

    ID = Column(Integer(), primary_key=True)
    RuTechnologyName = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)
    EnTechnologyName = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)
    column_num = 3
    column_names = ('ID', 'RuTechnologyName', 'EnTechnologyName')
    # relationship()

    def get_items_tuple(self):
        res = []
        res.extend([self.ID, self.RuTechnologyName, self.EnTechnologyName])
        return tuple(res)


class Diods(Base):
    __tablename__ = 'Diods'

    ID = Column(Integer(), primary_key=True)
    DocID = Column(BIGINT(), nullable=True)
    ComponentName = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=False, unique=False)

    Type_ID = Column(Integer(), ForeignKey('ComponentTypes.ID'), nullable=True)
    Kind_ID = Column(Integer(), ForeignKey('ComponentKinds.ID'), nullable=True)
    ManufacturerName_ID = Column(Integer(), ForeignKey('Manufacturers.ID'), nullable=True)

    MaxPermissibleDCVoltage = Column(FLOAT(), nullable=True)
    MinOperatingTemperature = Column(FLOAT(), nullable=True)
    MaxOperatingTemperature = Column(FLOAT(), nullable=True)
    MaxPermissibleAverageDirectCurrent = Column(FLOAT(), nullable=True)
    MaxiPermissibleDirectCurrent = Column(FLOAT(), nullable=True)
    RadiationResistance = Column(FLOAT(), nullable=True)
    RadiationResistanceI = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)
    QualicationSG = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)
    QualicationЕС = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)
    Package = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)
    Remark1 = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)
    Remark2 = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)
    column_num = 18
    column_names = ('ID', 'DocID', 'ComponentName', 'Type_ID', 'Kind_ID', 'ManufacturerName_ID',
                    'MaxPermissibleDCVoltage', 'MinOperatingTemperature', 'MaxOperatingTemperature',
                    'MaxPermissibleAverageDirectCurrent', 'MaxiPermissibleDirectCurrent',
                    'RadiationResistance', 'RadiationResistanceI', 'QualicationSG', 'QualicationЕС',
                    'Package', 'Remark1', 'Remark2')

    def get_items_tuple(self):
        res = []
        res.extend([self.ID, self.DocID, self.ComponentName, self.Type_ID, self. Kind_ID, self.ManufacturerName_ID,
                    self.MaxPermissibleDCVoltage,
                    self.MinOperatingTemperature, self.MaxOperatingTemperature,
                    self.MaxPermissibleAverageDirectCurrent, self.MaxiPermissibleDirectCurrent,
                    self.RadiationResistance, self.RadiationResistanceI,
                    self.QualicationSG, self.QualicationЕС, self.Package, self.Remark1, self.Remark2])
        return tuple(res)


class Resistors(Base):
    __tablename__ = 'Resistors'

    ID = Column(Integer(), primary_key=True)
    DocID = Column(BIGINT(), nullable=True)
    ComponentName = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=False, unique=False)

    Type_ID = Column(Integer(), ForeignKey('ComponentTypes.ID'), nullable=True)
    Kind_ID = Column(Integer(), ForeignKey('ComponentKinds.ID'), nullable=True)
    ManufacturerName_ID = Column(Integer(), ForeignKey('Manufacturers.ID'), nullable=True)
    PowerRating = Column(FLOAT(), nullable=True)
    MinVoltage = Column(FLOAT(), nullable=True)
    MaxVoltage = Column(FLOAT(), nullable=True)
    MinRatedResistance = Column(FLOAT(), nullable=True)
    MaxRatedResistance = Column(FLOAT(), nullable=True)
    ResistanceTolerance = Column(FLOAT(), nullable=True)
    MinOperatingTemperature = Column(FLOAT(), nullable=True)
    MaxOperatingTemperature = Column(FLOAT(), nullable=True)
    CurrentLimit = Column(FLOAT(), nullable=True)
    Package = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)
    QualicationSG = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)
    QualicationЕС = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)
    Remark1 = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)
    Remark2 = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)
    column_num = 20
    column_names = ('ID', 'DocID', 'ComponentName', 'Type_ID', 'Kind_ID', 'ManufacturerName_ID',
                    'PowerRating', 'MinVoltage', 'MaxVoltage',
                    'MinRatedResistance', 'MaxRatedResistance',
                    'ResistanceTolerance', 'MinOperatingTemperature', 'MaxOperatingTemperature', 'CurrentLimit',
                    'Package', 'QualicationSG', 'QualicationЕС', 'Remark1', 'Remark2')

    def get_items_tuple(self):
        res = []
        res.extend([self.ID, self.DocID, self.ComponentName, self.Type_ID, self. Kind_ID, self.ManufacturerName_ID,
                    self.PowerRating, self.MinVoltage, self.MaxVoltage, self.MinRatedResistance,
                    self.MaxRatedResistance, self.ResistanceTolerance,
                    self.MinOperatingTemperature, self.MaxOperatingTemperature,
                    self.CurrentLimit,  self.Package,
                    self.QualicationSG, self.QualicationЕС, self.Remark1, self.Remark2])
        return tuple(res)


class Transistors(Base):
    __tablename__ = 'Transistors'

    ID = Column(Integer(), primary_key=True)
    DocID = Column(BIGINT(), nullable=True)
    ComponentName = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=False, unique=False)

    Type_ID = Column(Integer(), ForeignKey('ComponentTypes.ID'), nullable=True)
    Kind_ID = Column(Integer(), ForeignKey('ComponentKinds.ID'), nullable=True)
    ManufacturerName_ID = Column(Integer(), ForeignKey('Manufacturers.ID'), nullable=True)

    MaxPermissibleDCVoltage = Column(FLOAT(), nullable=True)
    MinOperatingTemperature = Column(FLOAT(), nullable=True)
    MaxOperatingTemperature = Column(FLOAT(), nullable=True)
    MaxPermissibleDCCollectorCurrent = Column(FLOAT(), nullable=True)
    RadiationResistance = Column(FLOAT(), nullable=True)
    RadiationResistanceI = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)
    QualicationSG = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)
    QualicationЕС = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)
    Package = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)
    Remark1 = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)
    Remark2 = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)
    column_num = 17
    column_names = ('ID', 'DocID', 'ComponentName', 'Type_ID', 'Kind_ID', 'ManufacturerName_ID',
                    'MaxPermissibleDCVoltage', 'MinOperatingTemperature', 'MaxOperatingTemperature',
                    'MaxPermissibleDCCollectorCurrent', 'RadiationResistance', 'RadiationResistanceI',
                    'QualicationSG', 'QualicationЕС', 'Package', 'Remark1', 'Remark2')

    def get_items_tuple(self):
        res = []
        res.extend([self.ID, self.DocID, self.ComponentName, self.Type_ID, self. Kind_ID, self.ManufacturerName_ID,
                    self.MaxPermissibleDCVoltage,
                    self.MinOperatingTemperature, self.MaxOperatingTemperature,
                    self.MaxPermissibleDCCollectorCurrent,
                    self.RadiationResistance, self.RadiationResistanceI,
                    self.QualicationSG, self.QualicationЕС, self.Package, self.Remark1, self.Remark2])
        return tuple(res)


class Microchips(Base):
    __tablename__ = 'Microchips'

    ID = Column(Integer(), primary_key=True)
    DocID = Column(BIGINT(), nullable=True)
    ComponentName = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=False, unique=False)

    Type_ID = Column(Integer(), ForeignKey('ComponentTypes.ID'), nullable=False)
    Kind_ID = Column(Integer(), ForeignKey('ComponentKinds.ID'), nullable=False)
    ManufacturerName_ID = Column(Integer(), ForeignKey('Manufacturers.ID'), nullable=False)

    Interfaces = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)
    MinVoltage = Column(FLOAT(), nullable=False)
    MaxVoltage = Column(FLOAT(), nullable=False)
    Frequency = Column(FLOAT(), nullable=True)
    BitDepthValue = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)
    ConsumptionCurrent = Column(FLOAT(), nullable=True)
    TechnologyName_ID = Column(FLOAT(), ForeignKey('Technologies.ID'), nullable=False)
    MinOperatingTemperature = Column(FLOAT(), nullable=False)
    MaxOperatingTemperature = Column(FLOAT(), nullable=False)
    RadiationResistance = Column(FLOAT(), nullable=True)
    RadiationResistanceI = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)
    MemoryFormat = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)
    SamplingTime = Column(FLOAT(), nullable=True)
    Package = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)
    Qualication = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)
    Remark1 = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)
    column_num = 22
    column_names = ('ID', 'DocID', 'ComponentName', 'Type_ID', 'Kind_ID', 'ManufacturerName_ID',
                    'Interfaces', 'MinVoltage', 'MaxVoltage', 'Frequency', 'BitDepthValue',
                    'ConsumptionCurrent', 'TechnologyName_ID',
                    'MinOperatingTemperature', 'MaxOperatingTemperature',
                    'RadiationResistance', 'RadiationResistanceI',
                    'MemoryFormat', 'SamplingTime',
                    'Package', 'Qualication', 'Remark1')

    def get_items_tuple(self):
        res = []
        res.extend([self.ID, self.DocID, self.ComponentName, self.Type_ID, self. Kind_ID, self.ManufacturerName_ID,
                    self.Interfaces, self.MinVoltage, self.MaxVoltage, self.Frequency, self.BitDepthValue,
                    self.ConsumptionCurrent, self.TechnologyName_ID, self.MinOperatingTemperature,
                    self.MaxOperatingTemperature, self.RadiationResistance, self.RadiationResistanceI,
                    self.MemoryFormat, self.SamplingTime, self.Package, self.Qualication, self.Remark1])
        return tuple(res)


class Capacitors(Base):
    __tablename__ = 'Capacitors'

    ID = Column(Integer(), primary_key=True)
    DocID = Column(BIGINT(), nullable=True)
    ComponentName = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=False, unique=False)

    Type_ID = Column(Integer(), ForeignKey('ComponentTypes.ID'), nullable=True)
    Kind_ID = Column(Integer(), ForeignKey('ComponentKinds.ID'), nullable=True)
    ManufacturerName_ID = Column(Integer(), ForeignKey('Manufacturers.ID'), nullable=True)

    OutputType = Column(NVARCHAR(collation='Cyrillic_General_CI_AS'), nullable=True)
    MinVoltage = Column(DOUBLE(), nullable=True)
    MaxVoltage = Column(FLOAT(), nullable=True)
    MinCapacity = Column(FLOAT(), nullable=True)
    MaxCapacity = Column(FLOAT(), nullable=True)
    MinOperatingTemperature = Column(FLOAT(), nullable=True)
    MaxOperatingTemperature = Column(FLOAT(), nullable=True)
    AcceptableCapacityIncrease = Column(FLOAT(), nullable=True)
    AcceptableСapacityReduction = Column(FLOAT(), nullable=True)
    QualicationSG = Column(NVARCHAR(collation='Cyrillic_General_CI_AS'), nullable=True)
    QualicationЕС = Column(NVARCHAR(collation='Cyrillic_General_CI_AS'), nullable=True)
    Remark1 = Column(NVARCHAR(collation='Cyrillic_General_CI_AS'), nullable=True)
    Remark2 = Column(NVARCHAR(collation='Cyrillic_General_CI_AS'), nullable=True)
    column_num = 19
    column_names = ('ID', 'DocID', 'ComponentName', 'Type_ID', 'Kind_ID', 'ManufacturerName_ID',
                    'OutputType', 'MinVoltage', 'MaxVoltage',
                    'MinCapacity', 'MaxCapacity', 'MinOperatingTemperature', 'MaxOperatingTemperature',
                    'AcceptableCapacityIncrease', 'AcceptableСapacityReduction',
                    'QualicationSG', 'QualicationЕС', 'Remark1', 'Remark2')

    def get_items_tuple(self):
        res = []
        res.extend([self.ID, self.DocID, self.ComponentName, self.Type_ID, self. Kind_ID, self.ManufacturerName_ID,
                    self.OutputType, self.MinVoltage, self.MaxVoltage, self.MinCapacity, self.MaxCapacity,
                    self.MinOperatingTemperature, self.MaxOperatingTemperature,
                    self.AcceptableCapacityIncrease, self.AcceptableСapacityReduction,
                    self.QualicationSG, self.QualicationЕС, self.Remark1, self.Remark2])
        return tuple(res)


db_tables = (Microchips.__tablename__, Resistors.__tablename__, Diods.__tablename__, Capacitors.__tablename__,
             Transistors.__tablename__, Manufacturers.__tablename__, Technologies.__tablename__,
             ComponentKinds.__tablename__, ComponentTypes.__tablename__)


def create_tables(engine):
    Base.metadata.create_all(engine)
