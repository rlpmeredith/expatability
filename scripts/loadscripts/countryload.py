import csv
import numpy as np
from time import time
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


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

Base = declarative_base()


class Country(Base):
    __tablename__ = 'countries'

    country_or_territory = Column(String(64), primary_key=True)


if __name__ == "__main__":
    t = time()

    #Create the database engine
    engine = create_engine('mysql://admin:Leia0701!@localhost/expatability')
    Base.metadata.create_all(engine)

    #Create the session
    session = sessionmaker()
    session.configure(bind=engine)
    s = session()

    try:
        file_name = "../../data/ctry_capitals.csv"
        data = load_data(file_name)
        for i in data:
            record = Country(country_or_territory=i)
            s.add(record)

        s.commit()
    except:
        s.rollback()
    finally:
        s.close()
    print("Time elapsed: " + str(time() - t) + " s.")