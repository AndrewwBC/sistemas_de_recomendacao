import df_user_tracks
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

scaler = StandardScaler()
df = df_user_tracks.getDf()

columns = df.columns.drop(['user_id', 'track_id'])

df_user_features = df.groupby('track_id', as_index=False)[columns].mean()

X = df_user_features[columns].fillna(0)
X_scaled = scaler.fit_transform(X)

similarity = cosine_similarity(X_scaled)

similarity_df = pd.DataFrame(similarity)
print(similarity_df.head(5))
