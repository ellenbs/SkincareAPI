from fastapi import FastAPI, Query
import uvicorn
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np
import os

def load_reviews():
    current_dir = os.path.dirname(__file__)
    route = os.path.join(current_dir, "../data/sephora_reviews.csv")
    reviews = pd.read_csv(route)
    return reviews

def initialize_vectorizer(reviews):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(reviews['Review'])
    return vectorizer, X

app = FastAPI()
app.db = load_reviews()
app.vectorizer, app.X = initialize_vectorizer(app.db)

@app.get("/query")
def query_route(query: str = Query(..., description="Search query")):
    query_vector = app.vectorizer.transform([query])
    scores = np.array(app.X.dot(query_vector.T).todense()).flatten()

    app.db['Relevance Score'] = scores
    threshold = 0.01
    filtered_df = app.db[app.db['Relevance Score'] >= threshold]
    sorted_df = filtered_df.sort_values(by='Relevance Score', ascending=False)

    results = []
    for _, row in sorted_df.iterrows():
        results.append({
            'title': row['Nome'],
            'content': row['Review'][:500],
            'relevance': row['Relevance Score']
        })

    return {"results": results, "message": "OK"}

def run():
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    run()
