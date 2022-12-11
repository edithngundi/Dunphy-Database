from sqlalchemy.orm import sessionmaker  
from create import engine, Office, Agent, House, Sale, Commission
from datetime import date
from sqlalchemy import func

Session = sessionmaker(bind=engine)
session = Session()

#QUESTION 1:
#Find the top 5 offices with the most sales for that month.

#Using April for the queries
start = date(2022,4,1)
end = date(2022,4,30)

#find all the sales for each office in April and store them in sales
total_sales_per_office = (
    session
    .query(Office.name,
    func.sum(Sale.salePrice).label('sales'))
    .join(Agent, Sale.agent_ID == Agent.agentID)
    .join(Office, Agent.office_ID == Office.officeID)
    .filter(Sale.saleDate.between(start, end))
    .group_by(Office.officeID)
    .subquery()
)

#find the top 5 in the sales list
top_five_offices = (
    session
    .query(total_sales_per_office.c.name, total_sales_per_office.c.sales)
    .order_by(total_sales_per_office.c.sales.desc())
    .limit(5)   
)

#print the results
results = top_five_offices.all()
for result in results:
    print("---------------------------------------------------------")
    print(f"{result[0]}: {result[1]}")
    print("---------------------------------------------------------")

#QUESTION 2
#Find the top 5 estate agents who have sold the most for the month (include their contact details and their sales details so that it is easy contact them and congratulate them).

#find total sales for each agent in April, then find the top 5
top_five_agents = (
    session
    .query(Agent.firstname, Agent.lastname, Agent.phonenumber, func.sum(Sale.salePrice).label("sales"))
    .join(Sale, Agent.agentID == Sale.agent_ID)
    .filter(Sale.saleDate.between(start, end))
    .group_by(Agent.agentID)
    .order_by(func.sum(Sale.salePrice).desc())
    .limit(5)
)

#print results
for agent in top_five_agents:
    print("-----------------------------------------------------------------------------------")
    print(f"Agent: {agent.firstname} {agent.lastname},  " f"Phone number: {agent.phonenumber},  " f"Sales: {agent.sales}")
    print("-----------------------------------------------------------------------------------")

#QUESTION 3
#Calculate the commission that each estate agent must receive and store the results in a separate table.

#calculate commission based on saleprice
def calculate_commission(salePrice, agent_ID, commission):

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
    
    #update the commission table with new commission entries
    new_commission = Commission(commissionID=None, agent_ID=agent_ID, commission=commission)
    session.add(new_commission)
    session.commit()

#returns entries with the same agent ID in sale and commission table
comm_entries = (
    session
    .query(Sale, Commission)
    .join(Sale, Commission.agent_ID == Sale.agent_ID)
    .filter(Sale.saleDate.between(start, end))
    .all()
)

#all the commission entries, including initial 0 entries
commission_entries = session.query(Commission).all()

#delete all the existing entries as set in the initial commission table
for entry in commission_entries:
    session.delete(entry)

#save changes to the database
session.commit()

#loop through comm_entries and updates the appropriate commission value
for sale,entry in comm_entries:
    calculate_commission(sale.salePrice, sale.agent_ID, entry.commission)

#all new commission entries
commissions = session.query(Commission).all()

#print results
for commission in commissions:
    print("---------------------------------------------------------")
    print(f"Agent {commission.agent_ID}: {commission.commission}")
    print("---------------------------------------------------------")

#QUESTION 4
#For all houses that were sold that month, calculate the average number of days on the market.

#finds listing dates and sale dates of houses sold in April, and finds the average
average_days_on_market = (
    session
    .query(func.avg((func.julianday(Sale.saleDate) - func.julianday(House.listingDate))).label("Average Number of Days on Market"))
    .join(House, Sale.house_ID == House.houseID)
    .filter(Sale.saleDate.between(start, end))
    .all()
)

#print results
print("---------------------------------------------------------")
print(f"Average days on the market in April: {average_days_on_market[0][0]}")
print("---------------------------------------------------------")

#QUESTION 5
#For all houses that were sold that month, calculate the average selling price

#find sale prices for houses in April, and finds the average
average_sale_price = (
    session
    .query(func.avg(Sale.salePrice).label("average_salePrice"))
    .filter(Sale.saleDate
    .between(start,end))
    .all()
)

#print results
print("---------------------------------------------------------")
print(f"Average sale price in April: {average_sale_price[0][0]}")
print("---------------------------------------------------------")