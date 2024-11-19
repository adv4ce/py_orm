from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from params import params
from models import Base

DSN = f'postgresql://{params['login']}:{params['password']}@localhost:{params['localhost']}/{params['namedb']}'
engine = create_engine(DSN)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()