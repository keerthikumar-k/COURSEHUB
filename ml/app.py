from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle, os
from typing import List
import numpy as np

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

class RecommendRequest(BaseModel):
    userId: str
    enrolledCategories: List[str] = []

def load_model():
    if os.path.exists("model.pkl"):
        with open("model.pkl", "rb") as f:
            return pickle.load(f)
    return None

@app.post("/recommend")
def recommend(req: RecommendRequest):
    model = load_model()
    if not model:
        return {"recommendations": [], "message": "Model not trained yet"}

    courses = model["courses"]
    similarity = model["similarity"]

    if not req.enrolledCategories:
        # Return top popular courses
        recs = courses[:6]
        return {"recommendations": recs}

    # Find courses matching enrolled categories
    query_features = " ".join(req.enrolledCategories)
    from sklearn.feature_extraction.text import TfidfVectorizer
    tfidf = model["tfidf"]
    query_vec = tfidf.transform([query_features])

    import pandas as pd
    from sklearn.metrics.pairwise import cosine_similarity
    df = pd.DataFrame(courses)
    tfidf_matrix = tfidf.transform(df["features"])
    scores = cosine_similarity(query_vec, tfidf_matrix).flatten()

    top_indices = np.argsort(scores)[::-1][:6]
    recs = [courses[i] for i in top_indices]
    return {"recommendations": recs}

@app.get("/health")
def health():
    return {"status": "ok", "model_loaded": os.path.exists("model.pkl")}
