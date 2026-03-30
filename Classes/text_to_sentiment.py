import pickle
import os

def predict_sentiment(text):
    try:
        # Get current file path
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        # Correct paths for Render
        model_path = os.path.join(BASE_DIR, "../model.pkl")
        vectorizer_path = os.path.join(BASE_DIR, "../vectorizer.pkl")

        # Load model
        model = pickle.load(open(model_path, 'rb'))
        vectorizer = pickle.load(open(vectorizer_path, 'rb'))

        # Transform input
        vector = vectorizer.transform([text])

        prediction = model.predict(vector)[0]
        proba = model.predict_proba(vector)

        confidence = round(max(proba[0]) * 100, 2)

        sentiment = "Positive 😊" if prediction == 1 else "Negative 😠"

        return sentiment, confidence

    except Exception as e:
        return "Error", str(e)