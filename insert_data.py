#import necessary libraries
from sqlalchemy.orm import sessionmaker  
from create import engine, Office, Agent, Buyer, Seller, House, Sale, Commission
from datetime import date

#Initialize session
Session = sessionmaker(engine)
session = Session()

#Insert office data
office = [ 
           Office(officeID = 100, name = 'Dunphy HQ', location = 'Corona CA'),
           Office(officeID = 200, name = 'Dunphy Midd', location = 'Middlebury VT'),
           Office(officeID = 300, name = 'Dunphy Lafayette', location = 'Easton PA'),
           Office(officeID = 400, name = 'Dunphy Colgate', location = 'Hamilton NY'),
           Office(officeID = 500, name = 'Dunphy Rice', location = 'Houston TX'),
           Office(officeID = 600, name = 'Dunphy Young', location = 'Provo UT'),
           Office(officeID = 700, name = 'Dunphy Emerald', location = 'Seattle WA') 
        ]

#Insert agent data
agent = [ 
           Agent(agentID = 1, firstname = 'Kurt', lastname = 'Dwight', office_ID = 100, phonenumber = '1234567890'),
           Agent(agentID = 2, firstname = 'Scott', lastname = 'Michael', office_ID = 600, phonenumber = '4567890123'),
           Agent(agentID = 3, firstname = 'Pam', lastname = 'Halpert', office_ID = 300, phonenumber = '7890123456'),
           Agent(agentID = 4, firstname = 'Julie', lastname = 'Andrews', office_ID = 100, phonenumber = '0123456789'),
           Agent(agentID = 5, firstname = 'Mitchell', lastname = 'Pritchett', office_ID = 200, phonenumber = '3456789012'),
           Agent(agentID = 6, firstname = 'Bela', lastname = 'Maholtra', office_ID = 500, phonenumber = '6789012345'),
           Agent(agentID = 7, firstname = 'Kimberly', lastname = 'Murray', office_ID = 700, phonenumber = '9012345678'),
           Agent(agentID = 8, firstname = 'Leighton', lastname = 'Finkle', office_ID = 400, phonenumber = '2345678901'),
           Agent(agentID = 9, firstname = 'Jose', lastname = 'Alvarez', office_ID = 300, phonenumber = '5678901234') 
        ]

#Insert buyer data
buyer = [ 
           Buyer(buyerID = 10, firstname = 'Fena', lastname = 'Gitu', phonenumber = '0012345678'),
           Buyer(buyerID = 20, firstname = 'Wahiga', lastname = 'Mwaura', phonenumber = '0023456789'),
           Buyer(buyerID = 30, firstname = 'Chebet', lastname = 'Rono', phonenumber = '0034567890'),
           Buyer(buyerID = 40, firstname = 'Victoria', lastname = 'Rubadiri', phonenumber = '0045678901'),
           Buyer(buyerID = 50, firstname = 'Mark', lastname = 'Maasai', phonenumber = '0056789012')
        ]

#Insert seller data
seller = [ 
           Seller(sellerID = 11, firstname = 'Linus', lastname = 'Kaikai', phonenumber = '0067890123'),
           Seller(sellerID = 22, firstname = 'Kanze', lastname = 'Dena', phonenumber = '0078901234'),
           Seller(sellerID = 33, firstname = 'Lulu', lastname = 'Hassan', phonenumber = '0089012345'), 
           Seller(sellerID = 44, firstname = 'Mark', lastname = 'Maasai', phonenumber = '0056789012')
        ]

#Insert house listing data
house = [ 
           House(houseID = 1000, seller_ID = 11, bedrooms = 1, bathrooms = 1, listingPrice = 250000, zipcode = '10000', listingDate = date(2022,1,21), listingAgent = 1, listingOffice = 100, isSold = False),
           House(houseID = 2000, seller_ID = 22, bedrooms = 3, bathrooms = 2, listingPrice = 490000, zipcode = '20000', listingDate = date(2022,2,10), listingAgent = 5, listingOffice = 200, isSold = False),
           House(houseID = 3000, seller_ID = 33, bedrooms = 4, bathrooms = 4, listingPrice = 890000, zipcode = '30000', listingDate = date(2022,2,17), listingAgent = 9, listingOffice = 300, isSold = False),
           House(houseID = 4000, seller_ID = 11, bedrooms = 3, bathrooms = 1, listingPrice = 700000, zipcode = '40000', listingDate = date(2022,2,27), listingAgent = 8, listingOffice = 400, isSold = False),
           House(houseID = 5000, seller_ID = 22, bedrooms = 1, bathrooms = 1, listingPrice = 150000, zipcode = '50000', listingDate = date(2022,3,3), listingAgent = 7, listingOffice = 500, isSold = False),
           House(houseID = 6000, seller_ID = 33, bedrooms = 2, bathrooms = 1, listingPrice = 500000, zipcode = '10000', listingDate = date(2022,3,12), listingAgent = 4, listingOffice = 100, isSold = False),
           House(houseID = 7000, seller_ID = 11, bedrooms = 5, bathrooms = 3, listingPrice = 1100000, zipcode = '20000', listingDate = date(2022,4,11), listingAgent = 5, listingOffice = 200, isSold = False),
           House(houseID = 8000, seller_ID = 22, bedrooms = 2, bathrooms = 1, listingPrice = 430000, zipcode = '30000', listingDate = date(2022,4,13), listingAgent = 3, listingOffice = 300, isSold = False),
           House(houseID = 9000, seller_ID = 33, bedrooms = 1, bathrooms = 1, listingPrice = 400000, zipcode = '40000', listingDate = date(2022,4,19), listingAgent = 6, listingOffice = 400, isSold = False),
           House(houseID = 10000, seller_ID = 11, bedrooms = 2, bathrooms = 1, listingPrice = 300000, zipcode = '50000', listingDate = date(2022,4,25), listingAgent = 7, listingOffice = 500, isSold = False),
           House(houseID = 11000, seller_ID = 22, bedrooms = 1, bathrooms = 1, listingPrice = 70000, zipcode = '60000', listingDate = date(2022,5,8), listingAgent = 2, listingOffice = 600, isSold = False),
           House(houseID = 12000, seller_ID = 22, bedrooms = 2, bathrooms = 1, listingPrice = 200000, zipcode = '60000', listingDate = date(2022,5,20), listingAgent = 2, listingOffice = 600, isSold = False),
           House(houseID = 13000, seller_ID = 22, bedrooms = 3, bathrooms = 1, listingPrice = 750000, zipcode = '60000', listingDate = date(2022,5,21), listingAgent = 4, listingOffice = 100, isSold = False)   
        ]

#Insert sale data
sale = [
        Sale(saleID = 101, house_ID = 1000, buyer_ID = 10, agent_ID = 1, salePrice = 230000, saleDate = date(2022,4,1), commission = 0),
        Sale(saleID = 202, house_ID = 3000, buyer_ID = 20, agent_ID = 9, salePrice = 900000, saleDate = date(2022,4,3), commission = 0),
        Sale(saleID = 303, house_ID = 4000, buyer_ID = 50, agent_ID = 8, salePrice = 680000, saleDate = date(2022,4,7), commission = 0),
        Sale(saleID = 404, house_ID = 6000, buyer_ID = 40, agent_ID = 5, salePrice = 495000, saleDate = date(2022,4,21), commission = 0),
        Sale(saleID = 505, house_ID = 9000, buyer_ID = 30, agent_ID = 6, salePrice = 410000, saleDate = date(2022,4,26), commission = 0),
        Sale(saleID = 606, house_ID = 10000, buyer_ID = 20, agent_ID = 7, salePrice = 350000, saleDate = date(2022,4,28), commission = 0),
        Sale(saleID = 707, house_ID = 11000, buyer_ID = 40, agent_ID = 2, salePrice = 80000, saleDate = date(2022,5,12), commission = 0),
        Sale(saleID = 808, house_ID = 13000, buyer_ID = 30, agent_ID = 4, salePrice = 750000, saleDate = date(2022,5,23), commission = 0)   
        ]

#Insert commission data
commission = [
        Commission(commissionID = 1, agent_ID = 1, commission = 0),
        Commission(commissionID = 2, agent_ID = 9, commission = 0),
        Commission(commissionID = 3, agent_ID = 8, commission = 0),
        Commission(commissionID = 4, agent_ID = 5, commission = 0),
        Commission(commissionID = 5, agent_ID = 6, commission = 0),
        Commission(commissionID = 6, agent_ID = 7, commission = 0),
        Commission(commissionID = 7, agent_ID = 2, commission = 0),
        Commission(commissionID = 8, agent_ID = 4, commission = 0)
]

# Add multiple records of entries into tables
session.add_all(office)
session.add_all(agent)
session.add_all(buyer)
session.add_all(seller)
session.add_all(house)
session.commit()

session.add_all(sale)
session.add_all(commission)

#counter to autoincrement saleID
sale_counter = 1
def update_tables(saleID, house_ID, buyer_ID, agent_ID, salePrice, saleDate, commission):
    """
    Inserts commission entries in the sale table
    Updates the original listing status to SOLD

    Parameters:
        saleID (int) : Integer identifier for a sale
        house_ID (int) : Integer identifier that joins house and sale tables
        buyer_ID (int) : Integer identifier that joins buyer and sale tables
        agent_ID (int) : Integer identifier that joins agent and sale tables
        salePrice (int) : House selling price
        saleDate (date object) : Date of sale

    Returns:
        Updated sale table with new commission entries 
    """
    global sale_counter

    #for each new entry, update its saleID
    saleID = sale_counter
    sale_counter += 1

    #criteria for calculating commission
    if salePrice < 100000:
        commission = 0.1*salePrice
    elif salePrice >= 100000 and salePrice < 200000:
        commission = 0.075*salePrice
    elif salePrice >= 200000 and salePrice < 500000:
        commission = 0.06*salePrice
    elif salePrice >= 500000 and salePrice < 1000000:
        commission = 0.05*salePrice
    else:
        commission = 0.04*salePrice

    #add entries to the sale table
    new_sale = Sale(saleID=saleID, house_ID=house_ID, buyer_ID=buyer_ID, agent_ID=agent_ID, salePrice=salePrice, saleDate=saleDate, commission=commission)
    session.add(new_sale)
    session.commit()

    #update isSold in the house table to update listing status
    session.query(House).filter(House.houseID == house_ID).update({House.isSold: True})
    session.commit()

#update sale table entries with corresponding commission entries
sale_entries = session.query(Sale).all()
for entry in sale_entries:
    update_tables(saleID = entry.saleID, house_ID=entry.house_ID, buyer_ID=entry.buyer_ID, agent_ID=entry.agent_ID, salePrice=entry.salePrice, saleDate=entry.saleDate, commission=entry.commission)
session.commit()

#delete older entries of sale table
session.query(Sale).filter(Sale.saleID >= 101).delete()
session.commit()