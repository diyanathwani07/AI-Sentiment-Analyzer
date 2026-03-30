import streamlit as st
from Classes.text_to_sentiment import predict_sentiment

# Page config
st.set_page_config(page_title="AI Sentiment Analyzer", page_icon="💬", layout="centered")

# 🔥 CUSTOM CSS (IMPORTANT)
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #0f172a, #1e293b);
        color: white;
    }

    .main {
        background-color: rgba(255,255,255,0.03);
        padding: 30px;
        border-radius: 15px;
    }

    textarea {
        border-radius: 10px !important;
    }

    .stButton>button {
        background: #22c55e;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        border: none;
        transition: 0.3s;
    }

    .stButton>button:hover {
        background: #16a34a;
    }

    .result-box {
        padding: 20px;
        border-radius: 12px;
        margin-top: 20px;
        background: rgba(0,0,0,0.4);
        animation: fadeIn 0.5s ease-in-out;
    }

    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("💬 AI Sentiment Analyzer")

# Input
text = st.text_area("Enter your text:")

# Button
if st.button("Analyze"):
    if text.strip() != "":
        result, confidence = predict_sentiment(text)

        st.markdown(f"""
        <div class="result-box">
            <p><b>You entered:</b><br>{text}</p>
            <h2>{result}</h2>
            <p>Confidence: {confidence}%</p>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.warning("Please enter some text!")