from sqlalchemy import create_engine
import pandas as pd
import pymysql

df = pd.read_csv("D:/Data Analysis/OLA Project/Bookings-100000-Rows.csv")

engine = create_engine("mysql+pymysql://root:jatoimasab1122@localhost/OLA")

df.to_sql("Bookings", con=engine, if_exists="replace", index=False)
