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
        file_name = "../data/cost_living_index.csv"
        data = load_data(file_name)
        print(type(data))
        print(len(data))
        for i in data:
            record = models.Cost(capital=i[0], price_index=i[1],
                                      rank=i[2], avg_business_lunch=i[3],
                                      avg_rent_85m2_standard=i[4],
                                      public_trans_monthly=i[5]
                                      )
            s.add(record)
        s.commit()

    except Exception as e:
        print(e)
        s.rollback()

    finally:
        s.close()
    print("Time elapsed: " + str(time() - t) + " s.")