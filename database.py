from sqlalchemy import create_engine, Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class PoliceStation(Base):
    __tablename__ = 'police_stations'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    phone = Column(String)
    website = Column(String)
    address = Column(String)

engine = create_engine('sqlite:///police_stations.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
