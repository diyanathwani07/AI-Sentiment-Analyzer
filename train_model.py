import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

print("Training model...")

data = {
    'text': [
        'I love this product', 'Amazing experience', 'Very happy',
        'This is bad', 'Worst service ever', 'I hate this',
        'Not good', 'Excellent work', 'Terrible quality',
        'I am satisfied', 'Awful experience', 'Best purchase ever'
    ],
    'label': [1,1,1,0,0,0,0,1,0,1,0,1]
}

df = pd.DataFrame(data)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['text'])

model = MultinomialNB()
model.fit(X, df['label'])

pickle.dump(model, open('model.pkl','wb'))
pickle.dump(vectorizer, open('vectorizer.pkl','wb'))

print("✅ Model trained successfully!")