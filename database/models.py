# models.py
from sqlalchemy import Column, Integer, Float, String, DateTime, LargeBinary, Text, ForeignKey
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Customers(Base):
    __tablename__ = 'customers'
    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    contact_name = Column(String(50), nullable=False)
    address = Column(String(50))
    city = Column(String(50))
    postral_code = Column(String(50), nullable=False)
    country = Column(String(50), nullable=False)


class Employees(Base):
    __tablename__ = 'employees'
    employee_id = Column(Integer, primary_key=True, autoincrement=True)
    last_name = Column(String(50), nullable=False)
    first_name = Column(String(50), nullable=False)
    birth_date = Column(DateTime)
    photo = Column(LargeBinary)
    notes = Column(Text)


class Categories(Base):
    __tablename__ = 'categories'
    category_id = Column(Integer, primary_key=True, autoincrement=True)
    category_name = Column(String(50), nullable=False)
    description = Column(Text, nullable=False)


class Suppliers(Base):
    __tablename__ = 'suppliers'
    supplier_id = Column(Integer, primary_key=True, autoincrement=True)
    supplier_name = Column(String(50), nullable=False)
    contact_name = (String(50))
    address = Column(String(50), nullable=False)
    city = Column(String(50), nullable=False)
    postal_code = Column(String(50), nullable=False)
    country = Column(String(50), nullable=False)
    phone = Column(String(50))


class Shippers(Base):
    __tablename__ = 'shippers'
    shipper_id = Column(Integer, primary_key=True, autoincrement=True)
    shipper_name = Column(String(50), nullable=False)
    phone = Column(String(50), nullable=False)


class Orders(Base):
    __tablename__ = 'orders'
    order_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"), nullable=False)
    shipper_id = Column(Integer, ForeignKey("shippers.shipper_id"), nullable=False)
    employee_id = Column(Integer, ForeignKey("employees.employee_id"), nullable=False)
    order_date = Column(DateTime)


class Products(Base):
    __tablename__ = 'products'
    product_id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String(50), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.category_id"), nullable=False)
    supplier_id = Column(Integer,  ForeignKey("suppliers.supplier_id"),nullable=False)
    unit = Column(String(50))
    price = Column(Float, nullable=False)


class OrderDetails(Base):
    __tablename__ = 'order_details'
    order_details_id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer,  ForeignKey("orders.order_id"),nullable=False)
    product_id = Column(Integer, ForeignKey("products.product_id"), nullable=False)
    quantity = Column(Integer, nullable=False)

class Users(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    last_name = Column(String(50), nullable=False)
    first_name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    rol = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)

class Logs(Base):
    __tablename__ = 'logs'
    log_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    rol = Column(String(50), nullable=False)
    action = Column(String(50), nullable=False)
    date_time = Column(DateTime, nullable=False)
