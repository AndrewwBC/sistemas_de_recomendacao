import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from db import connection
conn = connection.openConnection()

def getDf():
    return  pd.read_sql("""
        SELECT 
        u.user_id, u.play_count, u.track_id, 
        t.energy, t.danceability, t.loudness, t.acousticness
        FROM users_tracks u
        LEFT JOIN tracks t ON (u.track_id = t.track_id) LIMIT 4000
        """, conn)