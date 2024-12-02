import streamlit as st
import pickle
import pandas as pd

# Loading pre-trained model and vectorizer
def load_model():
    with open("model.pkl", "rb") as model_file:
        model = pickle.load(model_file)
    with open("vectorizer.pkl", "rb") as vec_file:
        vectorizer = pickle.load(vec_file)
    return model, vectorizer

model, vectorizer = load_model()

# Streamlit app
st.title("Sentiment Analysis with Streamlit")
st.write("This app analyzes the sentiment of a given text (positive or negative) based on the Sentiment140 dataset.")

# Input box for user text
user_input = st.text_area("Enter a tweet or text to analyze:", "Streamlit is an amazing framework!")

if st.button("Analyze Sentiment"):
    if user_input.strip():
        # Vectorize input text
        input_vector = vectorizer.transform([user_input])
        # Predict sentiment
        prediction = model.predict(input_vector)[0]
        sentiment = "Positive" if prediction == 1 else "Negative"
        st.write(f"Predicted Sentiment: **{sentiment}**")
    else:
        st.write("Please enter some text to analyze.")
