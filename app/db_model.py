from sqlalchemy import String, Integer, Float, Column, create_engine, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from datetime import datetime

Base = declarative_base()
conn_password = "%40Mwangi254%25"
conn_string = f"mysql+mysqldb://root:{conn_password}@localhost/online_banking"
engine = create_engine(conn_string, echo=True)
Session =sessionmaker()

class Branch(Base):
    __tablename__ = "branches"
    id = Column(Integer(), primary_key=True)
    branch_name = Column(String(150), nullable=False, unique=True)
    branch_location =Column(String(100), nullable=False, unique=True)
    customer = relationship("Customer", backref="branches")

    def __repr__(self):
        return f"{self.branch_name}"

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer(), primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    username = Column(String(50), unique=True, nullable=False)
    id_number = Column(String(12), nullable=False, unique=True)
    email = Column(String(150), nullable=False)
    phone_no = Column(Integer(), nullable=False)
    password = Column(String(255), nullable=False)
    address = Column(String(50), nullable=False)
    branch_id = Column(Integer(), ForeignKey("branches.id"), nullable=True)
    created_at = Column(DateTime(), default=datetime.now())
    updated_at = Column(DateTime(), onupdate=datetime.now())
    account = relationship('Account', backref='user')


    def __repr__(self):
        return f"Customer {self.username} created at {self.created_at}"
    
class Account(Base):
    __tablename__ = "account"
    id = Column(Integer(), primary_key=True)
    account_number = Column(String(10), unique=True, nullable=True)
    account_type = Column(String(50), unique=True)
    balance = Column(Float(), default=0)
    customer_id = Column(Integer(), ForeignKey('customers.id'), nullable=False)
    transaction = relationship("Transaction", backref="account")


    def __repr__(self):
        return f" {self.account_number}"

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer(), primary_key=True)
    amount = Column(Float(), nullable=False)
    description = Column(String(200))
    timestamp = Column(DateTime(), default=datetime.now())
    account_id = Column(Integer(), ForeignKey('account.id'), nullable=True)


    def __repr__(self):
        return f" {self.description}"
    

Base.metadata.create_all(engine)
