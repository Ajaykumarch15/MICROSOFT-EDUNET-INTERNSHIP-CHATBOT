import streamlit as st
import google.generativeai as genai
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Set your API Key here
GENAI_API_KEY = "AIzaSyD7K45jsndpjkEUm4I52TJ2G_5cP0Ifiwg"  # 🔹 Replace with your actual key
genai.configure(api_key=GENAI_API_KEY)

# Load the Gemini AI model
model = genai.GenerativeModel("gemini-pro")


# Define AI-based healthcare chatbot
def healthcare_chatbot(user_input):
    response = model.generate_content(user_input)
    return response.text


# Streamlit web app interface
def main():
    st.title("Healthcare Assistant Chatbot 🏥")

    user_input = st.text_input("How can I assist you today?", "")

    if st.button("Submit"):
        if user_input:
            st.write("User: ", user_input)
            with st.spinner("Processing your query, please wait..."):
                response = healthcare_chatbot(user_input)
            st.write("Healthcare Assistant: ", response)
        else:
            st.warning("Please enter a query.")


if __name__ == "__main__":
    main()
