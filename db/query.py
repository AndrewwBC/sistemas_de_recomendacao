from conection import db
import pandas
query = db.cursor()

csvPath = "./tracks.csv"
read = pandas.read_csv(csvPath)
columns = read.columns

columnsToQuery = []

for col in columns:
    if(col == "Unnamed: 0"): 
        continue
    else:
        columnsToQuery.append(col)

columnsStr = ", ".join(columnsToQuery)

def createQuery(sql, values):
    query.execute(sql, values)
    return query
    
placeholders = ", ".join(["%s"] * len(columnsToQuery))

for index, row in read.iterrows():
    values = ([row[col] for col in columnsToQuery])
    if(row["track_id"] != "1kR4gIb7nGxHPI3D2ifs59"):
        createQuery(f'INSERT INTO tracks({columnsStr}) VALUES({placeholders}) ON CONFLICT (track_id) DO NOTHING RETURNING track_id', values)

db.commit()
query.close()
db.close()