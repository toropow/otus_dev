from sqlalchemy import Column, Integer, String, Boolean

from .database import db


class Student(db.Model):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
