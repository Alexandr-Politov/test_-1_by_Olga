from sqlalchemy import Column, Integer, String, DECIMAL, DATETIME, func

from data_base.engine import Base


class DBProduct(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(127), nullable=False, unique=True)
    description = Column(String(511), nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
    created_at = Column(DATETIME, default=func.now())
