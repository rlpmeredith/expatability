import csv
import os
from time import time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from application import models

# Configure SQL Alchemy logging

import logging

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.DEBUG)


db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')
db_host = os.environ.get('DB_HOST')
db_schema = os.environ.get('DB_SCHEMA')


# Function to load csv data and return list

def load_data(file_name):

    with open(file_name) as f:
        reader = csv.reader(f, delimiter=',' )
        next(reader)
        data = list(reader)

    return data


if __name__ == "__main__":
    t = time()
    Base = declarative_base()

    #Create the database engine
    engine = create_engine(f'mysql://{db_user}:{db_password}@{db_host}/{db_schema}?charset=utf8', encoding='utf-8')
    Base.metadata.create_all(engine)

    #Create the session
    session = sessionmaker()
    session.configure(bind=engine)
    s = session()

    try:
        file_name = "../data/average-weather.csv"
        data = load_data(file_name)
        print(type(data))
        print(len(data))
        for i in data:
            print(type(i[1]))
            cap = i[0]
            if i[1] != '':
                jan = int(i[1])
            else:
                jan = None
            if i[2] != '':
                jul = int(i[2])
            else:
                jul = None
            record = models.AvgWeather(capital=cap, jan_avg=jan, july_avg=jul)
            s.add(record)
            print(i)
        s.commit()

    except Exception as e:
        print(e)
        s.rollback()

    finally:
        s.close()
    print("Time elapsed: " + str(time() - t) + " s.")