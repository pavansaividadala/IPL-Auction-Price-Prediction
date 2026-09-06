import streamlit as st
import pandas as pd
import pickle

# Load model
with open("xgb_ipl_auction_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("IPL Auction Price Prediction")

Player_Name = st.text_input("Player Name")

# ---- NUMERICAL INPUTS ----
Age = st.number_input("Age", min_value=16, value=25)
Matches = st.number_input("Matches Played", min_value=0, value=30)
Experience = st.number_input("Experience (in Yrs)", min_value=0, value=5)
Runs = st.number_input("Runs", min_value=0, value=500)
Strike_Rate = st.number_input("Strike Rate", min_value=0.0, value=130.0)
Wickets = st.number_input("Wickets", min_value=0, value=10)
Economy = st.number_input("Economy", min_value=0.0, value=8.0)
Average = st.number_input("Average", min_value=0.0, value=28.0)

# ---- CATEGORICAL INPUTS ----
Country = st.selectbox("Country", ["India", "Australia", "England", "South Africa", "New Zealand", "West Indies", "Sri Lanka", "Bangladesh", "Afghanistan", "Other"])
Role = st.selectbox("Role", ["Batsman", "Bowler", "All-Rounder", "Wicket-Keeper"])
Team_Preference = st.selectbox("Team_Preference", ["MI", "CSK",  "RCB", "KKR", "SRH", "DC", "PBKS", "RR", "GT", "LSG"])

# ---- CREATE INPUT DATAFRAME (EXACT COLUMN NAMES) ----
input_data = pd.DataFrame({
    "Age": [Age],
    "Country": [Country],
    "Role": [Role],
    "Matches": [Matches],
    "Experience ( in Yrs)": [Experience],
    "Runs": [Runs],
    "Strike_Rate": [Strike_Rate],
    "Wickets": [Wickets],
    "Economy": [Economy],
    "Average": [Average],
    "Team_Preference": [Team_Preference]
})

# ---- PREDICTION ----
if st.button("Predict Auction Price"):
    if Player_Name.strip() == "":
        st.warning("Please enter the player's name.")
    else:
        prediction = model.predict(input_data)
        st.success(f"Player: {Player_Name}")
        st.success(f"Predicted Auction Price: ₹{prediction[0]:.2f} Cr")