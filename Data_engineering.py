import pandas as pd
import numpy as np

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String, Float
import pymysql
pymysql.install_as_MySQLdb()
####################### Import Statements end ##################################
hawaii_measurement_path = "Resources/hawaii_measurements.csv"
hawaii_station_path = "Resources/hawaii_stations.csv"


measurementsdf = pd.read_csv(hawaii_measurement_path)
measurementsdf


stationsdf = pd.read_csv(hawaii_station_path)
stationsdf

clean_measurements = measurementsdf[measurementsdf['prcp'].isna()]
clean_measurements

type(clean_measurements['date'][0])


clean_measurements.to_csv('clean_measurements.csv')

############ Database insertion operations #################
