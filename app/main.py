import streamlit as st
from sentiment_model import predict_sentiment

# Set the title of the app
st.markdown("<h1 style='color: #4545a7;'>Sentiment Analysis App</h1>", unsafe_allow_html=True)

# Instruction for the user
st.markdown("<h4 style='color: darkgray;'>Enter your text below to analyze sentiment:</h4>", unsafe_allow_html=True)

# Text input from the user
text = st.text_area("", height=150, help="Type the text you want to analyze here.")

# Check if there is input text
if text:
    # Display a spinner while processing
    with st.spinner('Analyzing sentiment...'):
        try:
            # Obtain sentiment scores from the model
            scores = predict_sentiment(text)
            
            # Convert scores to percentages
            positive_percent = scores[2] * 100
            neutral_percent = scores[1] * 100
            negative_percent = scores[0] * 100
            
            # Display sentiment scores
            st.markdown("### Sentiment Scores")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown(f"<h2 style='text-align: center; color: #26C281;'>Positive</h2><h3 style='text-align: center;'>{positive_percent:.2f}%</h3>", unsafe_allow_html=True)
            with col2:
                st.markdown(f"<h2 style='text-align: center; color: #FFDD57;'>Neutral</h2><h3 style='text-align: center;'>{neutral_percent:.2f}%</h3>", unsafe_allow_html=True)
            with col3:
                st.markdown(f"<h2 style='text-align: center; color: #FA2A00;'>Negative</h2><h3 style='text-align: center;'>{negative_percent:.2f}%</h3>", unsafe_allow_html=True)
        
        except Exception as e:
            # Handle any exceptions that occur during sentiment analysis
            st.error(f"An error occurred: {e}")

st.markdown("---")
st.info("Powered by cardiffnlp/twitter-roberta-base-sentiment-latest. Developed by Najib Aghenda.")