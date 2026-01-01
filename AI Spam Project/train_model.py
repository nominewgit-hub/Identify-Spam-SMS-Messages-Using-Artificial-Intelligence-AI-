import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load dataset
df = pd.read_csv("spam.csv", encoding="latin1")
df = df[['v1','v2']]
df.columns = ['label','message']
df['label'] = df['label'].map({'ham':0,'spam':1})

# TF-IDF (FIT HERE)
tfidf = TfidfVectorizer(max_features=3000)
X = tfidf.fit_transform(df['message'])
y = df['label']

# Train model
model = MultinomialNB()
model.fit(X, y)

# SAVE FITTED OBJECTS
pickle.dump(tfidf, open("vectorizer.pkl", "wb"))
pickle.dump(model, open("model.pkl", "wb"))

print("✅ Training complete. Files saved.")
