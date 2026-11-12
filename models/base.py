import os
from dotenv import load_dotenv

from sqlalchemy import Engine, create_engine,make_url
from sqlalchemy.orm import DeclarativeBase

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')


class BaseModel(DeclarativeBase):
    ...


def get_engine() -> Engine:
    url = make_url(DATABASE_URL).set(drivername='postgresql+psycopg')
    return create_engine(url)
