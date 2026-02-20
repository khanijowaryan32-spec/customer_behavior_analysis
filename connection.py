import psycopg2
from sqlalchemy import create_engine
import pandas as pd 

df = pd.read_csv("customer_data.csv")
conn = psycopg2.connect(
    user = "aryan_khanijow" , 
    password = "1234" , 
    database = "company_sales" , 
    host = "localhost" , 
    port = "5432"
)

print("connected")

username = "aryan_khanijow" 
password = "1234" 
database = "company_sales"  
host = "localhost" 
port = "5432"

engine = create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}")
df.to_sql(
    name="data" , 
    con=engine , 
    if_exists="replace" , 
    index=False
)
