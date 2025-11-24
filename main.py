import sys
import os
import pyodbc

from scheduler.reader import PDFParser
from scheduler import launcher, UnitOfWork, Resistors
print(pyodbc.drivers())

sys.path.append(os.path.dirname(__file__))
# launcher.start()

# db = UnitOfWork()
# db.mkdir(Resistors.__tablename__)
# db.insert_many(Resistors.__tablename__)
# db.insert_many(Microchips.__tablename__)





