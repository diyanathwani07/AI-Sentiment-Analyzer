import pickle

def predict_sentiment(text):
    model = pickle.load(open('model.pkl','rb'))
    vectorizer = pickle.load(open('vectorizer.pkl','rb'))

    vector = vectorizer.transform([text])
    prediction = model.predict(vector)[0]
    proba = model.predict_proba(vector)

    confidence = round(max(proba[0]) * 100, 2)

    sentiment = "Positive 😊" if prediction == 1 else "Negative 😠"

    return sentiment, confidence