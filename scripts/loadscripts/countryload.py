import numpy as np
import csv
from time import time
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def load_data(file_name, file_name_2):

    country1list = []
    country2list = []

    with open(file_name) as f:
        reader1 = csv.reader(f, delimiter=',' )
        next(reader1)
        list1 = list(reader1)
    for country1 in list1:
        country1list.append(country1[1])

    with open(file_name_2) as f2:
        reader2 = csv.reader(f2, delimiter=',' )
        next(reader2)
        list2 = list(reader2)
    for country2 in list2:
        country2list.append(country2[0])

    data = np.unique(country1list + country2list)
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
        file_name = "../../data/world_happiness.csv"
        file_name_2 = "../../data/immigrant.csv"
        data = load_data(file_name, file_name_2)
        for i in data:
            print(i)
            record = Country(country_or_territory=i)
            s.add(record)

        s.commit()
    except:
        s.rollback()
    finally:
        s.close()
    print("Time elapsed: " + str(time() - t) + " s.")