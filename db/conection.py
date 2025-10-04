import psycopg2

db = psycopg2.connect(database = "psr", 
    user = "postgres", 
    host= 'localhost',
    password = "1234",
    port = 5432)

