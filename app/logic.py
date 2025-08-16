from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import random

def build_recommender(movies_df):
    tfidf = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf.fit_transform(movies_df["title"])
    return tfidf_matrix

def recommend_movies(title, movies_df, tfidf_matrix, top_n=5):
    index = movies_df[movies_df["title"].str.lower() == title.lower()].index
    if index.empty:
        return []
    idx = index[0]
    cosine_sim = cosine_similarity(tfidf_matrix[idx], tfidf_matrix).flatten()
    similar_indices = cosine_sim.argsort()[::-1][1:top_n + 1]
    return movies_df.iloc[similar_indices].to_dict(orient="records")

def get_random_movie(movies_df):
    return movies_df.sample(1).iloc[0].to_dict()

