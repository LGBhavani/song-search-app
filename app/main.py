from fastapi import FastAPI
from app.recommender import SongSearch

app = FastAPI(title="Song Search & Suggested API")

recommender = SongSearch("data/spotify_millsongdata.csv")

@app.get("/")
def home():
    return {"message": "Song Search & Suggested API"}


@app.get("/recommend")
def recommend(song: str):
    results = recommender.recommend(song)
    if not results:
        return {"error": "Song not found"}
    return {
        "input_song": song,
        "suggested_songs": results
    }
