from langchain_groq import ChatGroq  # Changed this line
from dotenv import load_dotenv
import os
import streamlit as st
from langchain import PromtTemplate

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

st.title("LangChain Demo With Groq")

input_text = st.text_input("Search the topic you want")

llm = ChatGroq(
    groq_api_key=groq_api_key,
    model="llama-3.1-8b-instant",
    temperature=0.8
)

if input_text:
    response = llm.invoke(input_text)
    st.write(response.content)