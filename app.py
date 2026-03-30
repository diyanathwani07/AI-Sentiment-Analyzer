import streamlit as st
from Classes.text_to_sentiment import predict_sentiment

st.set_page_config(page_title="AI Sentiment Analyzer", page_icon="💬")

st.title("💬 AI Sentiment Analyzer")

text = st.text_area("Enter your text:")

if st.button("Analyze"):
    if text.strip() != "":
        result, confidence = predict_sentiment(text)

        st.subheader("Result")
        st.write(f"**You entered:** {text}")
        st.success(result)
        st.info(f"Confidence: {confidence}%")
    else:
        st.warning("Please enter some text!")