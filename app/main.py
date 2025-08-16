from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import numpy as np
from app.data import load_movies, load_reviews
from app.logic import build_recommender, recommend_movies, get_random_movie

app = FastAPI()

# 👇 Add this block
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or ["http://localhost:5500"] if using Live Server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

movies_df = load_movies()
reviews_df = load_reviews()
tfidf_matrix = build_recommender(movies_df)

def clean_df(df: pd.DataFrame):
    """Ensure all values are JSON-safe by replacing NaN, Inf."""
    return df.replace({np.nan: None, np.inf: None, -np.inf: None}).to_dict(orient="records")

@app.get("/search")
def search_movie(query: str):
    results = movies_df[movies_df["title"].str.contains(query, case=False)]
    return clean_df(results[["slug", "title", "year"]])

@app.get("/recommendations/{slug}")
def get_recommendations(slug: str):
    movie_row = movies_df[movies_df["slug"] == slug]
    if movie_row.empty:
        raise HTTPException(status_code=404, detail="Movie not found.")
    title = movie_row.iloc[0]["title"]
    recs = recommend_movies(title, movies_df, tfidf_matrix)
    return clean_df(pd.DataFrame(recs))

@app.get("/movie/{slug}")
def get_movie_reviews(slug: str):
    movie_reviews = reviews_df[reviews_df["movie_slug"] == slug]
    if movie_reviews.empty:
        raise HTTPException(status_code=404, detail="No reviews found.")
    return clean_df(movie_reviews[["review", "stars"]])

@app.get("/roulette")
def roulette():
    movie = get_random_movie(movies_df)
    slug = movie["slug"]
    title = movie["title"]

    movie_reviews = reviews_df[reviews_df["movie_slug"] == slug]
    safe_reviews = movie_reviews[["review", "stars"]].where(pd.notnull(movie_reviews), None).to_dict(orient="records")

    return {
        "slug": slug,
        "title": title,
        "reviews": safe_reviews
    }

