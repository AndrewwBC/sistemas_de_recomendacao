from connection import db

query = db.cursor()

def createQuery(sql, values):
    query.execute(sql, values)
    rows = query.fetchall()
    return rows