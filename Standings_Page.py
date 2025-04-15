import streamlit as st
import requests
import pandas as pd

st.title("NFL Team Standings (SportsData.io API)")

API_KEY = "a250f05817e64885bdf4fa870dcd37da"  

season = "2024"  

url = f"https://api.sportsdata.io/v3/nfl/scores/json/Standings/{season}"

headers = {
    "Ocp-Apim-Subscription-Key": API_KEY
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()

    df = pd.DataFrame(data)
    df = df[["Team", "Division", "Wins", "Losses", "PointsFor", "PointsAgainst"]]
    df = df.sort_values(by="Wins", ascending=False)

    st.subheader(f"NFL Standings - {season} Season")
    st.dataframe(df)

    st.bar_chart(df.set_index("Team")[["Wins"]])

else:
    st.error(f"Failed to fetch standings. Status Code: {response.status_code}")
    st.text(response.text)
