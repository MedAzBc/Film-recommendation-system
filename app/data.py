import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def load_movies(path=os.path.join(BASE_DIR, "movies.csv")):
    return pd.read_csv(path)

def load_reviews(path=os.path.join(BASE_DIR, "reviews.csv")):
    return pd.read_csv(path)

