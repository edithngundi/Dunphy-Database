#import necessary libraries
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, ForeignKey, Date, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base

#connect with database
engine = create_engine('sqlite:///db_application_assignment.db', echo=True)
engine.connect()

#mark classes with the tables
Base = declarative_base()

#classes for the database schema
class Office(Base):
    """
    Table for office data
    """
    __tablename__ = 'office'
    officeID = Column(Integer(), primary_key=True)
    name = Column(String(30), nullable=False, unique=True)
    location = Column(String(30), nullable=False, unique=True)

    def __init__(self, officeID, name, location):
        self.officeID = officeID
        self.name = name
        self.location = location

class Agent(Base):
    """
    Table for agent data
    """
    __tablename__ = 'agent'
    agentID = Column(Integer(), primary_key=True)
    firstname = Column(String(30), nullable=False)
    lastname = Column(String(30), nullable=False)
    office_ID = Column(Integer(), ForeignKey('office.officeID'), index=True)
    phonenumber = Column(String(20), nullable=False)

    def __init__(self, agentID, firstname, lastname, office_ID, phonenumber):
        self.agentID = agentID
        self.firstname = firstname
        self.lastname = lastname
        self.office_ID = office_ID
        self.phonenumber = phonenumber

class Buyer(Base):
    """
    Table for buyer data
    """
    __tablename__ = 'buyer'
    buyerID = Column(Integer(), primary_key=True)
    firstname = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=False)
    phonenumber = Column(String(20), nullable=False)

    def __init__(self, buyerID, firstname, lastname, phonenumber):
        self.buyerID = buyerID
        self.firstname = firstname
        self.lastname = lastname
        self.phonenumber = phonenumber

class Seller(Base):
    """
    Table for seller data
    """
    __tablename__ = 'seller'
    sellerID = Column(Integer(), primary_key=True)
    firstname = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=False)
    phonenumber = Column(String(20), nullable=False)

    def __init__(self, sellerID, firstname, lastname, phonenumber):
        self.sellerID = sellerID
        self.firstname = firstname
        self.lastname = lastname
        self.phonenumber = phonenumber

class House(Base):
    """
    Table for house listing data
    """
    __tablename__ = 'house'
    houseID =  Column(Integer(), primary_key=True)
    seller_ID = Column(Integer(), ForeignKey('seller.sellerID'), index = True)
    bedrooms = Column(Integer())
    bathrooms = Column(Integer())
    listingPrice = Column(Integer())
    zipcode = Column(String(10))
    listingDate = Column(Date())
    listingAgent = Column(Integer(), ForeignKey('agent.agentID'), index = True)
    listingOffice = Column(Integer(), ForeignKey('office.officeID'), index = True)
    isSold = Column(Boolean(), default=False)

    def __init__(self, houseID, seller_ID, bedrooms, bathrooms, listingPrice, zipcode, listingDate, listingAgent, listingOffice, isSold):
        self.houseID = houseID
        self.seller_ID = seller_ID
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.listingPrice = listingPrice
        self.zipcode = zipcode
        self.listingDate = listingDate
        self.listingAgent = listingAgent
        self.listingOffice = listingOffice
        self.isSold = isSold  

class Sale(Base):
    """
    Table for house sale data
    """
    __tablename__ = 'sale'
    saleID = Column(Integer(), primary_key=True, autoincrement=True)
    house_ID = Column(Integer(), ForeignKey('house.houseID'))
    agent_ID = Column(Integer(), ForeignKey('agent.agentID'), index = True)
    buyer_ID = Column(Integer(), ForeignKey('buyer.buyerID'))
    salePrice = Column(Integer())
    saleDate = Column(Date())
    commission = Column(Float())

    def __init__(self, saleID, house_ID, agent_ID, buyer_ID, salePrice, saleDate, commission):
        self.saleID = saleID
        self.house_ID = house_ID
        self.agent_ID = agent_ID
        self.buyer_ID = buyer_ID
        self.salePrice = salePrice
        self.saleDate = saleDate
        self.commission = commission

class Commission(Base):
    """
    Table for commission data
    """
    __tablename__ = 'commission'
    commissionID = Column(Integer(), primary_key=True, autoincrement=True)
    agent_ID = Column(Integer(), ForeignKey('agent.agentID'))
    commission = Column(Float())

    def __init__(self, commissionID, agent_ID, commission):
        self.commissionID = commissionID
        self.agent_ID = agent_ID
        self.commission = commission

#create schema in database and bind it to the engine
Base.metadata.create_all(bind=engine)