#PANDA PROGRAM TO READ SQL FILE
import pandas as pd
from sqlalchemy import create_engine

# Create a SQLAlchemy engine object
engine = create_engine('mysql+mysqlconnector://root:Kavya@1512@localhost/try')

# Open a connection
conn = engine.connect()

# Read data from the MySQL table
data = pd.read_sql("SELECT * FROM movie", conn)

# Close the connection
conn.close()

print(type(data))