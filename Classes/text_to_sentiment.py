import pickle
import os

# 🔥 Load ONCE (not inside function)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, "../model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "../vectorizer.pkl")

model = pickle.load(open(model_path, 'rb'))
vectorizer = pickle.load(open(vectorizer_path, 'rb'))


def predict_sentiment(text):
    try:
        vector = vectorizer.transform([text])

        prediction = model.predict(vector)[0]
        proba = model.predict_proba(vector)

        confidence = round(max(proba[0]) * 100, 2)

        sentiment = "Positive 😊" if prediction == 1 else "Negative 😠"

        return sentiment, confidence

    except Exception as e:
        return "Error", str(e)