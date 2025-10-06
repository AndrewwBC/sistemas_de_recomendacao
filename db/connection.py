import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

db_user = os.getenv("DB_USER")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_pass = os.getenv("DB_PASS")

def openConnection():
    return psycopg2.connect(database = "psr", 
    user = db_user, 
    host= db_host,
    password = db_pass,
    port = db_port)
    
db = openConnection()
print(db)