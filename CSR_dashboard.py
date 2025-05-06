import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

# Simulated user data generator
def generate_users(n=50):
    regions = ['Trivandrum', 'Kollam', 'Kochi', 'Alappuzha', 'Global']
    teams = ['GreenWizards', 'EcoStars', 'PlanetSavers', 'CarbonCutters']
    users = []

    for i in range(n):
        user = {
            "username": f"User{i+1}",
            "total_co2_saved": random.randint(10, 150),
            "streak_count": random.randint(1, 30),
            "region": random.choice(regions),
            "team": random.choice(teams),
            "participation": {
                "Public Transport Week": random.choice([True, False]),
                "Plastic Free Challenge": random.choice([True, False]),
                "Tree Planting Month": random.choice([True, False])
            }
        }
        users.append(user)
    return users

user_data_list = generate_users(50)
df = pd.DataFrame(user_data_list)

# Calculate participation %
def calculate_participation(df, challenge_name):
    return round((df['participation'].apply(lambda x: x.get(challenge_name, False)).sum() / len(df)) * 100, 2)

def csr_dashboard():
    st.title("🌏 CSR Partner Dashboard")

    # Team selector
    teams = df['team'].unique().tolist()
    selected_team = st.selectbox("Select Corporate Team", ["All Teams"] + teams)

    # Filter data based on team selection
    team_df = df if selected_team == "All Teams" else df[df['team'] == selected_team]

    st.markdown(f"### 📊 Dashboard for: **{selected_team}**")

    # 1. Total Carbon Savings
    total_savings = team_df['total_co2_saved'].sum()
    st.subheader("Total Carbon Savings")
    st.write(f"**{total_savings} kg CO₂** saved by users in this team.")

    # 2. Participation Rates
    st.subheader("Participation in Sponsored Challenges")
    challenges = ["Public Transport Week", "Plastic Free Challenge", "Tree Planting Month"]
    participation_rates = {
        challenge: calculate_participation(team_df, challenge) for challenge in challenges
    }
    participation_df = pd.DataFrame(participation_rates.items(), columns=["Challenge", "Participation Rate (%)"])
    st.bar_chart(participation_df.set_index("Challenge"))

    # 3. ESG and SDG Reporting
    st.subheader("Impact Highlights (ESG & SDG)")
    st.markdown("""
    - 🌍 **SDG 13 - Climate Action**: CO₂ savings contribute directly to reducing emissions.
    - 🚌 **SDG 11 - Sustainable Cities**: Public transport participation boosts city sustainability.
    - 🌿 **SDG 12 - Responsible Consumption**: Plastic-free efforts reduce waste.
    """)

    # 4. Brand Visibility (static example)
    st.subheader("Brand Visibility Metrics")
    brand_visibility = {"logo_impressions": 15000, "mentions": 300}
    st.write(f"Logo Impressions: {brand_visibility['logo_impressions']}")
    st.write(f"Mentions: {brand_visibility['mentions']}")

    # Bar chart for brand visibility
    fig, ax = plt.subplots()
    ax.bar(brand_visibility.keys(), brand_visibility.values(), color=['#4CAF50', '#2196F3'])
    ax.set_title("Brand Visibility")
    st.pyplot(fig)

    # 5. Sponsor Custom Challenge
    st.subheader("Sponsor a Custom Challenge")
    challenge_name = st.text_input("Enter Challenge Name")
    if st.button("Sponsor Challenge"):
        st.success(f"🎉 Challenge '{challenge_name}' has been sponsored for **{selected_team}**!")

# Run the dashboard
if __name__ == "__main__":
    csr_dashboard()
