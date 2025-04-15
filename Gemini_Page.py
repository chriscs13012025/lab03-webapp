import streamlit as st
import requests
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

st.title("🏀 NBA Matchup Analyzer (Powered by Gemini)")
st.write("Pick two NBA teams and let Gemini analyze the matchup based on mock win records.")

MOCK_WINS = {
    "Los Angeles Lakers": 43,
    "Boston Celtics": 57,
    "Miami Heat": 44,
    "Golden State Warriors": 46,
    "Milwaukee Bucks": 49,
    "Phoenix Suns": 47,
    "Denver Nuggets": 53,
    "New York Knicks": 50
}

teams = list(MOCK_WINS.keys())

team1 = st.selectbox("Select Team 1", teams)
team2 = st.selectbox("Select Team 2", teams)

if team1 != team2 and st.button("Generate Gemini Preview"):
    prompt = (
        f"Write an NBA matchup preview between {team1} and {team2}.\n"
        f"{team1} has {MOCK_WINS[team1]} wins this season, "
        f"{team2} has {MOCK_WINS[team2]}.\n"
        f"Compare their strengths, weaknesses, and predict a winner."
    )
    
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    st.markdown("### 🧠 Gemini's Analysis")
    st.write(response.text)
