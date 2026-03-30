from flask import Flask, render_template, request
from Classes.text_to_sentiment import predict_sentiment
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['text']

    try:
        result, confidence = predict_sentiment(text)
    except Exception as e:
        result = "Error"
        confidence = "0"
        print(e)

    return render_template(
        'home.html',
        user_text=text,
        prediction=result,
        confidence=confidence
    )

# Render compatible run
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))