from db import connection

db = connection.db

query = db.cursor()

def createQuery(sql, values = 0):
    query.execute(sql, values)
    rows = query.fetchall()
    db.commit()
    return rows

