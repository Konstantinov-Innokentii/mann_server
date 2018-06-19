from .db import Base
from sqlalchemy import Column, Integer, Time


class Dinner(Base):

    __tablename__ = "dinner"

    id = Column(Integer, primary_key=True)
    size = Column(Integer, nullable=False)
    date = Column(Time, nullable=False)

    def __repr__(self):
        return "Dinner {}'".format(self.id)

    def __str__(self):
        return "Dinner {} {}".format(self.size, self.date)
