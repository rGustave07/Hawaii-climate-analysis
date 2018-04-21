from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String, Float, Date
import pymysql
pymysql.install_as_MySQLdb()
########################## Import Statements end ##########################

# Creating classes for db
class Measurements(Base):
    __tablename__ = 'measurements'
    id = Column(Integer, primary_key = True)
    station = Column(String(255))
    date = Column(String(255))
    prcp = Column(Float)
    tobs = Column(Integer)


class Stations(Base):
    __tablename__ = 'stations'
    id = Column(Integer, primary_key = True)
    station = Column(String(255))
    name = Column(String(255))
    latitude = Column(Float)
    longitude = Column(Float)
    elevation = Column(Float)


engine = create_engine("sqlite:///hawaii.sqlite")
Base.metadata.create_all(engine)
