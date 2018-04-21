import pandas as pd
import numpy as np
import os

import sqlalchemy
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric, Text, Float
########## Import Statements #########################

hawaii_measurement_path = "Resources/hawaii_measurements.csv"
hawaii_station_path = "Resources/hawaii_stations.csv"
clean_hawaii_measurements = "Resources/clean_measurements.csv"

df = pd.read_csv(clean_hawaii_measurements)
df



data = df.to_dict(orient='records')
data[0]

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
metadata = MetaData(bind=engine)
metadata.reflect()

table = sqlalchemy.Table('measurements', metadata, autoload = True)
conn = engine.connect()

dfstation = pd.read_csv(hawaii_station_path)
dfstation


datastations = dfstation.to_dict(orient = "records")
datastations

stationtable = sqlalchemy.Table('stations', metadata, autoload = True)
conn.execute(stationtable.insert(), datastations)


conn.execute("SELECT * FROM stations").fetchall()

conn.execute(table.insert(), data)
conn.execute("SELECT * FROM measurements").fetchall()
