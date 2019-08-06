from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime


Base = declarative_base()


class Rating(Base):
    __tablename__ = 'ratings'
    id = Column(Integer, primary_key=True)
    device = Column(String)
    date = Column(DateTime)
    rating = Column(Integer)

    def __repr__(self):
        return "<Rating(device='{}', date='{}', rating='{}'>".format(self.device,
                                                                     self.date,
                                                                     self.rating)

    def __str__(self):
        return "<Rating(device='{}', date='{}', rating='{}'>".format(self.device,
                                                                     self.date,
                                                                     self.rating)
