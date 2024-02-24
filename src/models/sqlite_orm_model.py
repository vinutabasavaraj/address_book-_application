from sqlalchemy import Column, Float, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class AddressModel(Base):
  __tablename__ = "addresses"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String)
  street = Column(String)
  city = Column(String)
  state = Column(String)
  zip_code = Column(String)
  latitude = Column(Float)
  longitude = Column(Float)
