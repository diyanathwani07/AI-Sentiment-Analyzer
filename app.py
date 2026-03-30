from flask import Flask, render_template, request

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('home.html')


# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['text']

    try:
        from Classes.text_to_sentiment import predict_sentiment
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


# Run app
if __name__ == "__main__":
    app.run(debug=True)