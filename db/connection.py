import psycopg2

def openConnection():
    return psycopg2.connect(database = "psr", 
    user = "postgres", 
    host= 'localhost',
    password = "1234",
    port = 5432)
    
db = openConnection()