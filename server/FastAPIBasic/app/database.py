# import time

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import settings

# import psycopg2
# from psycopg2.extras import RealDictCursor

# from . import models
# from .database import engine

# models.Base.metadata.create_all(bind=engine)

SQLALCHEMY_DATABASE_URL = settings.POSTGRES_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# while True:
#     try:
#         conn = psycopg2.connect(
#             host="localhost",
#             database='fastapi',
#             user='postgres',
#             password='postgres',
#             cursor_factory=RealDictCursor
#         )
#         cursor = conn.cursor()
#         print("db connected")
#
#         break
#
#     except Exception as error:
#         print("db connection failed")
#         print(error)
#
#         time.sleep(2)
