from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Publisher(Base):
  __tablename__ = 'publisher'

  id = Column(Integer, primary_key=True)
  name = Column(String, nullable=False, unique=True)


class Book(Base):
  __tablename__ = 'book'

  id = Column(Integer, primary_key=True)
  title = Column(String, nullable=False)
  id_publisher = Column(Integer, ForeignKey('publisher.id'))

  publisher = relationship(Publisher, backref='publisher')



class Shop(Base):
  __tablename__ = 'shop'

  id = Column(Integer, primary_key=True)
  name = Column(String, nullable=False)



class Stock(Base):
  __tablename__ = 'stock'

  id = Column(Integer, primary_key=True)
  count = Column(Integer, nullable=False)
  id_book = Column(Integer, ForeignKey('book.id'))
  id_shop = Column(Integer, ForeignKey('shop.id'))

  book = relationship(Book, backref='book')
  shop = relationship(Shop, backref='shop')



class Sale(Base):
  __tablename__ = 'sale'

  id = Column(Integer, primary_key=True)
  price = Column(Float, nullable=False)
  date_sale = Column(DateTime, nullable=False)
  count = Column(Integer, nullable=False)
  id_stock = Column(Integer, ForeignKey('stock.id'))

  stock = relationship(Stock, backref='stock')