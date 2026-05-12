from sqlalchemy import create_engine, Column, Integer, String, Date, Time, ForeignKey, CheckConstraint
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

DATABASE_URL = "postgresql://postgres:sky@localhost:5432/postgres"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

try:
    dept = Department(department_name='Кафедра ДВРПАЗУ', department_head_name='Иванов О.П.')
    session.add(dept)
    session.commit()
    print("q")
except Exception as e:
    session.rollback()
    print(e)
finally:
    session.close()