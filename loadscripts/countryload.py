import csv
import numpy as np
import os
from time import time
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from application import models

# Configure SQL Alchemy logging

import logging

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')
db_host = os.environ.get('DB_HOST')
db_schema = os.environ.get('DB_SCHEMA')

# Function to load data from csv file and return a unique list

def load_data(file_name):

    finallist =[]
    with open(file_name) as f:
        reader = csv.reader(f, delimiter=',' )
        next(reader)
        country_list = list(reader)
    for country in country_list:
        finallist.append(country[0])

    data = np.unique(finallist)
    return data.tolist()

if __name__ == "__main__":
    t = time()
    Base = declarative_base()

    #Create the database engine
    engine = create_engine(f'mysql://{db_user}:{db_password}@{db_host}/{db_schema}')
    Base.metadata.create_all(engine)

    #Create the session
    session = sessionmaker()
    session.configure(bind=engine)
    s = session()

    try:
        file_name = "../data/ctry_capitals.csv"
        data = load_data(file_name)
        for i in data:
            record = models.Country(country_or_territory=i)
            s.add(record)
        s.commit()

    except Exception as e:
        print(e)
        s.rollback()

    finally:
        s.close()
    print("Time elapsed: " + str(time() - t) + " s.")