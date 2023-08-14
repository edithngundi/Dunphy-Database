## Description
A simple database system for a fictitious real estate company (Dunphy Real Estate) written in Python using SQLAlchemy. The company has many offices located all over the country. Each office is responsible for selling houses in a particular area. However an estate agent can be associated with one or more offices.

[program]

## Features of the database
- [x] 1. Defines the following tables: office, agent, buyer, seller, house, sale, and commission.
- [x] 2. For querying purposes, tables are linked with unique foreign keys.
- [x] 3. Listing prices and sale prices are different in some cases.
- [x] 4. Commissions are calculated on a sliding scale based on sale prices, and added as entries into the sale and commission tables.
- [x] 5. Once a successful sale is made, the listing status of a house is marked as sold.

## Implemented queries
- [x] 1. Find the top 5 offices with the most sales for that month.
- [x] 2. Find the top 5 estate agents who have sold the most for the month (including their contact details and their sales details).
- [x] 3. Calculate the commission that each estate agent must receive for the month and store the results in a separate table.
- [x] 4. For all houses that were sold that month, calculate the average number of days on the market.
- [x] 5. For all houses that were sold that month, calculate the average selling price.

## Running the Program
To execute all the relevant parts of the code, run the following commands:

### MacOS
```bash
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
python3 create.py
python3 delete_db.py
python3 insert_data.py
python3 query_data.py
python3 testing.py
```

### Windows
```cmd
python3 -m venv venv
venv\Scripts\activate.bat
pip3 install -r requirements.txt
python3 create.py
python3 delete_db.py
python3 insert_data.py
python3 query_data.py
python3 testing.py
```

- The `create.py` file creates a schema in the database and bind it to the engine.
- The `delete_db.py` file deletes all the data in the database. It was useful in development.
- The `insert_data.py` file inserts entries into the tables.
- The `query_data.py` file performs the 5 queries outlined earlier.
- The `testing.py` file runs unit tests to ensure the queries are performed correctly.

### Best practices
 Data normalization: This is the process of organizing a database into tables and columns in such a way that the data is stored in the most efficient and non-redundant way possible. This database is normalized because data is stored in separate tables for each entity and relationships are maintained using foreign keys. In the code, primary keys are defined as 'nameID' and foreign keys as 'name_ID'. The only redundancy however is in the sale and commission tables where both have commission columns. The commission table is unnecessary but was executed for purposes of the 3rd query. The commissions are stored better in the sale table.
