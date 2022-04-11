from os import environ
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

host=environ['eightqueen_host']
password=environ['eightqueen_password']
user=environ['eightqueen_user']
database=environ['eightqueen_database']
engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}/{database}")

Session = sessionmaker(engine)

with Session() as session:
    Base = declarative_base()
