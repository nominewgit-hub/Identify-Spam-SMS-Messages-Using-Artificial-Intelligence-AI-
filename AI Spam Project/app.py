import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

nltk.download('punkt')
nltk.download('stopwords')

ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = [i for i in text if i.isalnum()]
    y = [i for i in y if i not in stopwords.words('english')]
    y = [ps.stem(i) for i in y]

    return " ".join(y)

# LOAD fitted objects
tfidf = pickle.load(open("vectorizer.pkl", "rb"))
model = pickle.load(open("model.pkl", "rb"))

st.title("Identify spam SMS messages using AI")

input_sms = st.text_area("Below is a free classifier to identify spam SMS messages. Just input your text, and our AI will predict if it's spam - in just seconds.")

if st.button("Predict"):
    transformed_sms = transform_text(input_sms)
    vector_input = tfidf.transform([transformed_sms])
    result = model.predict(vector_input)[0]

    if result == 1:
        st.error("🚫 Spam Message")
    else:
        st.success("✅ Not Spam")