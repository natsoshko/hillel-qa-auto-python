from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:postgres_6949@127.0.0.1:5432/hillel_db"
engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)

def get_session():
    return Session()