from numpy import genfromtxt
from time import time
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def Load_Data(file_name):
    data = genfromtxt(file_name, delimiter=',', skip_header=1, dtype='unicode', converters={0: lambda s: str(s)})
    return data.tolist()

Base = declarative_base()

class Country(Base):
    __tablename__ = 'countries'

    country_or_territory = Column(String(64), primary_key=True)


if __name__ == "__main__":
    t = time()

    #Create the database
    engine = create_engine('mysql://admin:Leia0701!@localhost/expatability')
    Base.metadata.create_all(engine)

    #Create the session
    session = sessionmaker()
    session.configure(bind=engine)
    s = session()

    try:
        file_name = "../../data/world_happiness.csv"
        data = Load_Data(file_name)
        print(type(data))
        print(len(data))
        for i in data:
            print(i)
            record = Country(country_or_territory=i[1])
            s.add(record)

        s.commit()
    except:
        s.rollback()
    finally:
        s.close()
    print("Time elapsed: " + str(time() - t) + " s.")