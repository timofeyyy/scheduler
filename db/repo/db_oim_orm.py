import datetime

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import NVARCHAR, BIGINT, FLOAT, DOUBLE, DATE, SMALLINT
from sqlalchemy.dialects import mssql


Base = declarative_base()


class Manufacturers(Base):
    __tablename__ = 'Manufacturers'

    ID = Column(Integer(), primary_key=True)
    ManufacturerName = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)
    CountryID = Column(Integer(), ForeignKey('Countries.ID'), nullable=True)

    Capacitors = relationship('Capacitors', backref='Manufacturers')
    Resistors = relationship('Resistors', backref='Manufacturers')
    Diods = relationship('Diods', backref='Manufacturers')
    Microchips = relationship('Microchips', backref='Manufacturers')
    Transistors = relationship('Transistors', backref='Manufacturers')


class Countries(Base):
    __tablename__ = 'Countries'

    ID = Column(Integer(), primary_key=True)
    ForeignNative = Column(mssql.TINYINT(), ForeignKey('Foreignness.ID'), nullable=True)

    CountryName = Column(NVARCHAR(100, collation='Cyrillic_General_CI_AS'), nullable=False, unique=True)
    Manufacturers = relationship('Manufacturers', backref='Countries')


class Foreignness(Base):
    __tablename__ = 'Foreignness'

    ID = Column(mssql.TINYINT(), primary_key=True)
    ForeignName = Column(NVARCHAR(100, collation='Cyrillic_General_CI_AS'), nullable=False, unique=True)
    Countries = relationship('Countries', backref='Foreignness')


class ComponentKinds(Base):
    __tablename__ = 'ComponentKinds'

    ID = Column(Integer(), primary_key=True)
    RuComponentKind = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)
    EnComponentKind = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)
    Capacitors = relationship('Capacitors', backref='ComponentKinds')


class ComponentTypes(Base):
    __tablename__ = 'ComponentTypes'

    ID = Column(Integer(), primary_key=True)
    RuComponentType = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)
    EnComponentType = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)
    Capacitors = relationship('Capacitors', backref='ComponentTypes')


class Technologies(Base):
    __tablename__ = 'Technologies'

    ID = Column(Integer(), primary_key=True)
    RuTechnologyName = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)
    EnTechnologyName = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)


class Diods(Base):
    __tablename__ = 'Diods'
    __typename__ = "Diod"

    ID = Column(Integer(), primary_key=True, info={"skip": True})
    DocID = Column(BIGINT(), nullable=True, info={"skip": True})
    ComponentName = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=False, unique=False, info={"compare": True})
    Insertion = Column(DATE(), nullable=True, default=datetime.datetime.now(), info={"skip": True})

    Type_ID = Column(Integer(), ForeignKey('ComponentTypes.ID'), nullable=True, info={"skip": True})
    Kind_ID = Column(Integer(), ForeignKey('ComponentKinds.ID'), nullable=True, info={"skip": True})
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
    SpecificationDoc = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)


class Resistors(Base):
    __tablename__ = 'Resistors'
    __typename__ = "Resistor"

    ID = Column(Integer(), primary_key=True, autoincrement=True, info={"skip": True})
    DocID = Column(BIGINT(), nullable=True, info={"skip": True})
    ComponentName = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=False, unique=False, info={"compare": True})
    Insertion = Column(DATE(), nullable=True, default=datetime.datetime.now(), info={"skip": True})
    Type_ID = Column(Integer(), ForeignKey('ComponentTypes.ID'), nullable=True, info={"skip": True})
    Kind_ID = Column(Integer(), ForeignKey('ComponentKinds.ID'), nullable=True, info={"skip": True})
    ManufacturerName_ID = Column(Integer(), ForeignKey('Manufacturers.ID'), nullable=True)
    PowerRating = Column(FLOAT(), nullable=True)
    MinVoltage = Column(FLOAT(), nullable=True)
    MaxVoltage = Column(FLOAT(), nullable=True)
    MinRatedResistance = Column(FLOAT(), nullable=True, info={"compare": True})
    MaxRatedResistance = Column(FLOAT(), nullable=True)
    ResistanceTolerance = Column(FLOAT(), nullable=True)
    MinOperatingTemperature = Column(FLOAT(), nullable=True)
    MaxOperatingTemperature = Column(FLOAT(), nullable=True)
    CurrentLimit = Column(FLOAT(), nullable=True)
    Package = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)
    QualicationSG = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)
    QualicationЕС = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)
    Remark1 = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False, info={"skip": True})
    Remark2 = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False, info={"skip": True})
    SpecificationDoc = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)


class Transistors(Base):
    __tablename__ = 'Transistors'
    __typename__ = "Transistor"

    ID = Column(Integer(), primary_key=True, info={"skip": True})
    DocID = Column(BIGINT(), nullable=True, info={"skip": True})
    ComponentName = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=False, unique=False, info={"compare": True})
    Insertion = Column(DATE(), nullable=True, default=datetime.datetime.now(), info={"skip": True})

    Type_ID = Column(Integer(), ForeignKey('ComponentTypes.ID'), nullable=True, info={"skip": True})
    Kind_ID = Column(Integer(), ForeignKey('ComponentKinds.ID'), nullable=True, info={"skip": True})
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
    SpecificationDoc = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)


class Microchips(Base):
    __tablename__ = 'Microchips'
    __typename__ = "Microchip"


    ID = Column(Integer(), primary_key=True, autoincrement=True, info={"skip": True})
    DocID = Column(BIGINT(), nullable=True, info={"skip": True})
    ComponentName = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=False, unique=False, info={"compare": True})
    Insertion = Column(DATE(), nullable=True, default=datetime.datetime.now(), info={"skip": True})
    Type_ID = Column(Integer(), ForeignKey('ComponentTypes.ID'), nullable=False, info={"skip": True})
    Kind_ID = Column(Integer(), ForeignKey('ComponentKinds.ID'), nullable=False, info={"skip": True})
    ManufacturerName_ID = Column(Integer(), ForeignKey('Manufacturers.ID'), nullable=False)

    Interfaces = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)
    MinVoltage = Column(FLOAT(), nullable=False, default=0)
    MaxVoltage = Column(FLOAT(), nullable=False, default=0)
    Frequency = Column(FLOAT(), nullable=True)
    BitDepthValue = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)
    ConsumptionCurrent = Column(FLOAT(), nullable=True)
    TechnologyName_ID = Column(Integer(), ForeignKey('Technologies.ID'), nullable=False, info={"skip": True})
    MinOperatingTemperature = Column(FLOAT(), nullable=False, default=0)
    MaxOperatingTemperature = Column(FLOAT(), nullable=False, default=0)
    RadiationResistance = Column(FLOAT(), nullable=True)
    RadiationResistanceI = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)
    MemoryFormat = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)
    SamplingTime = Column(FLOAT(), nullable=True)
    Package = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)
    Qualication = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)
    Remark1 = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)
    SpecificationDoc = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)


class Capacitors(Base):
    __tablename__ = 'Capacitors'
    __typename__ = "Capacitor"

    ID = Column(Integer(), primary_key=True, info={"skip": True})
    DocID = Column(BIGINT(), nullable=True,info={"skip": True})
    ComponentName = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=False, unique=False, info={"compare": True})
    Insertion = Column(DATE(), nullable=True, default=datetime.datetime.now(), info={"skip": True})

    Type_ID = Column(Integer(), ForeignKey('ComponentTypes.ID'), nullable=True, info={"skip": True})
    Kind_ID = Column(Integer(), ForeignKey('ComponentKinds.ID'), nullable=True, info={"skip": True})
    ManufacturerName_ID = Column(Integer(), ForeignKey('Manufacturers.ID'), nullable=True)

    OutputType = Column(NVARCHAR(collation='Cyrillic_General_CI_AS'), nullable=True)
    MinVoltage = Column(FLOAT(), nullable=True)
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
    SpecificationDoc = Column(NVARCHAR(450, collation='Cyrillic_General_CI_AS'), nullable=True, unique=False)


def create_tables(engine):
    Base.metadata.create_all(engine)
