#import data from create.py file
from create import *

def delete_db(engine_in_use):
    """
    Function that deletes all the data in the database
    Parameters:
        engine_in_use : Current engine object
    Returns: 
        Empty database
    """
    Base.metadata.drop_all(bind=engine_in_use)

if __name__ == "__main__":
    delete_db(engine)