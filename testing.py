from sqlalchemy.orm import sessionmaker  
from create import engine, Office, Agent, House, Sale, Commission, Seller, Buyer
from datetime import date
from sqlalchemy import func
import unittest
from query_data import calculate_commission

class Tests(unittest.TestCase):

    #create session and bind it to the engine
    Session = sessionmaker(bind=engine)
    session = Session()

    def test_1_link_1(self):
        """
        Tests whether the link between sale and house tables is correct
        """
        sale = self.session.query(Sale).filter(Sale.saleID == 2).first()
        house = self.session.query(House).filter(House.houseID == sale.house_ID).first()

        #check that the house ID in the sale and house tables are the same
        self.assertEqual(sale.house_ID, house.houseID)

    def test_2_link_2(self):
        """
        Tests whether the link between office and agent tables is correct
        """
        agent = self.session.query(Agent).filter(Agent.agentID == 1).first()
        office = self.session.query(Office).filter(Office.officeID == agent.office_ID).first()

        #check that the office ID in the office and agent tables are the same
        self.assertEqual(agent.office_ID, office.officeID)

    def test_3_link_3(self):
        """
        Tests whether the link between house and seller tables is correct
        """
        house = self.session.query(House).filter(House.houseID == 1000).first()
        seller = self.session.query(Seller).filter(Seller.sellerID == house.seller_ID).first()

        #check that the seller ID in the seller and house tables are the same
        self.assertEqual(house.seller_ID, seller.sellerID)

    def test_4_link_4(self):
        """
        Tests whether the link between sale and buyer tables is correct
        """
        sale = self.session.query(Sale).filter(Sale.saleID == 1).first()
        buyer = self.session.query(Buyer).filter(Buyer.buyerID == sale.buyer_ID).first()

        #check that the buyer ID in the sale and buyer tables are the same
        self.assertEqual(sale.buyer_ID, buyer.buyerID)

    def test_5_link_5(self):
        """
        Tests whether the link between sale and agent tables is correct
        """
        sale = self.session.query(Sale).filter(Sale.saleID == 3).first()
        agent = self.session.query(Agent).filter(Agent.agentID == sale.agent_ID).first()

        #check that the agent ID in the sale and agent tables are the same
        self.assertEqual(sale.agent_ID, agent.agentID)
    
    def test_6_link_6(self):
        """
        Tests whether the link between house and office tables is correct
        """
        house = self.session.query(House).filter(House.houseID == 2000).first()
        office = self.session.query(Office).filter(Office.officeID == house.listingOffice).first()

        #check that the office ID in the office and house tables are the same
        self.assertEqual(house.listingOffice, office.officeID)

    def test_7_link_7(self):
        """
        Tests whether the link between commission and agent tables is correct
        """
        commission = self.session.query(Commission).filter(Commission.commissionID == 4).first()
        agent = self.session.query(Agent).filter(Agent.agentID == commission.agent_ID).first()

        #check that the agent ID in the commission and agent tables are the same
        self.assertEqual(commission.agent_ID, agent.agentID)
    
    def test_8_top_offices(self):
        """
        Tests the query for finding top offices of the month
        """
        
        #start and end dates for the test
        self.start = date(2022,4,1)
        self.end = date(2022,4,30)

        expected_results = [
            ['Dunphy Lafayette', 900000],
            ['Dunphy Colgate', 680000],
            ['Dunphy Midd', 495000]
        ]

        #finds the top 3 offices of the month
        total_sales_per_office = (
            self.session
            .query(Office.name, func.sum(Sale.salePrice).label("sales"))
            .join(Agent, Sale.agent_ID == Agent.agentID)
            .join(Office, Agent.office_ID == Office.officeID)
            .filter(Sale.saleDate.between(self.start, self.end))
            .group_by(Office.officeID)
            .subquery()
        )
        top_three_offices = (
            self.session
            .query(total_sales_per_office.c.name, total_sales_per_office.c.sales)
            .order_by(total_sales_per_office.c.sales.desc())
            .limit(3)
        )
        
        results = []
        for office in top_three_offices:
            results.append([office.name, office.sales])
            print(results)

        self.assertEqual(results, expected_results)
    
    def test_9_calculate_commission(self):
        """
        Tests the calculation of commission
        """

        #arbitrary sale prices, agent IDs, and commissions initialized at 0
        calculate_commission(100000, 10, 0)
        calculate_commission(199000, 11, 0)
        calculate_commission(350000, 12, 0)
        calculate_commission(670000, 13, 0)
        calculate_commission(1000000, 14, 0)

        #retrieves the updated commission entries
        commission1 = self.session.query(Commission).filter(Commission.agent_ID == 10).first()
        commission2 = self.session.query(Commission).filter(Commission.agent_ID == 11).first()
        commission3 = self.session.query(Commission).filter(Commission.agent_ID == 12).first()
        commission4 = self.session.query(Commission).filter(Commission.agent_ID == 13).first()
        commission5 = self.session.query(Commission).filter(Commission.agent_ID == 14).first()

        #checks that the commission calculated is the same as expected results
        self.assertEqual(commission1.commission, 7500)
        self.assertEqual(commission2.commission, 14925)
        self.assertEqual(commission3.commission, 21000)
        self.assertEqual(commission4.commission, 33500)
        self.assertEqual(commission5.commission, 40000)

    def test_10_average_days_on_market(self):
        """
        Tests the calculation of average days in the market
        """
        #start and end dates for the test
        self.start = date(2022,5,1)
        self.end = date(2022,5,30)

        #calculate average days on market
        average_days_on_market = (
        self.session
        .query(func.avg((func.julianday(Sale.saleDate) - func.julianday(House.listingDate))).label("Average_days_on_the_market"))
        .join(House, Sale.house_ID == House.houseID)
        .filter(Sale.saleDate.between(self.start, self.end))
        .all()
        )

        #check that the average is equal to the expected result
        self.assertEqual(average_days_on_market[0][0], 3)

    def test_11_top_three_agents(self):
        """
        Tests the query for finding top agents of the month
        """
        #start and end dates for the test
        self.start = date(2022,4,1)
        self.end = date(2022,4,30)

        expected_results = [
            ['Jose', 'Alvarez', '5678901234', 900000],
            ['Leighton', 'Finkle', '2345678901', 680000],
            ['Mitchell', 'Pritchett', '3456789012', 495000]
            ]
        
        #finds the top 3 agents of the month
        top_three_agents = (
            self.session
            .query(Agent.firstname, Agent.lastname, Agent.phonenumber, func.sum(Sale.salePrice).label("sales"))
            .join(Sale, Agent.agentID == Sale.agent_ID)
            .filter(Sale.saleDate.between(self.start, self.end))
            .group_by(Agent.agentID)
            .order_by(func.sum(Sale.salePrice).desc())
            .limit(3)
        )

        results = []
        for agent in top_three_agents:
            results.append([agent.firstname, agent.lastname, agent.phonenumber, agent.sales])
            print(results)

        self.assertEqual(results, expected_results)

    def test_12_average_sale_price(self):
        """
        
        """

        #start and end dates for the test
        self.start = date(2022,5,1)
        self.end = date(2022,5,30)

        average_sale_price = (
            self.session
            .query(func.avg(Sale.salePrice).label("average_salePrice"))
            .filter(Sale.saleDate
            .between(self.start,self.end))
            .all()
        )

        #check that the average is equal to the expected result
        self.assertEqual(average_sale_price[0][0], 415000)

if __name__ == "__main__":
    unittest.main()