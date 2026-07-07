import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle, os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def get_data():
    client = MongoClient(os.getenv("MONGO_URI"))
    db = client["course_management"]
    courses = list(db.courses.find({}, {"_id": 1, "title": 1, "category": 1, "description": 1, "level": 1}))
    enrollments = list(db.enrollments.find({}, {"userId": 1, "courseId": 1}))
    client.close()
    return courses, enrollments

def train_and_save():
    courses, enrollments = get_data()
    if not courses:
        print("No courses found. Add courses first.")
        return

    df = pd.DataFrame(courses)
    df["_id"] = df["_id"].astype(str)
    df["features"] = df["category"] + " " + df["level"] + " " + df["title"]

    tfidf = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf.fit_transform(df["features"])
    similarity = cosine_similarity(tfidf_matrix)

    model = {"courses": df.to_dict("records"), "similarity": similarity, "tfidf": tfidf}
    with open("model.pkl", "wb") as f:
        pickle.dump(model, f)
    print(f"Model trained with {len(courses)} courses.")

if __name__ == "__main__":
    train_and_save()
