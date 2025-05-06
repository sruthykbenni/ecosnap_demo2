import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Simulated user data for demonstration purposes
user_data = {
    "username": "EcoWarrior",
    "daily_savings": 1.5,  # kg CO₂ saved today
    "weekly_savings": 10.5,  # kg CO₂ saved this week
    "monthly_savings": 45.0,  # kg CO₂ saved this month
    "historical_activity": {
        "dates": pd.date_range(start="2023-01-01", periods=30, freq='D'),
        "savings": np.random.uniform(0.5, 2.0, size=30)  # Random savings for the last 30 days
    },
    "streak_count": 7,  # Current streak in days
    "milestones": [5, 10, 15],  # Achieved milestones
    "savings_by_category": {
        "Travel": 20.0,
        "Waste": 15.0,
        "Energy": 10.0
    },
    "regional_average": 30.0,  # kg CO₂ saved by the average user in the region
    "global_average": 25.0  # kg CO₂ saved by the global average user
}

def display_personal_dashboard():
    st.title(f"{user_data['username']}'s Personal Dashboard 📈")

    # CO₂ Savings Summary
    st.subheader("CO₂ Savings Summary")
    st.write(f"**Daily Savings:** {user_data['daily_savings']} kg")
    st.write(f"**Weekly Savings:** {user_data['weekly_savings']} kg")
    st.write(f"**Monthly Savings:** {user_data['monthly_savings']} kg")

    # Historical Activity
    st.subheader("Historical Eco-Snap Activity ")
    historical_df = pd.DataFrame({
        "Date": user_data["historical_activity"]["dates"],
        "Savings (kg)": user_data["historical_activity"]["savings"]
    })
    st.line_chart(historical_df.set_index("Date"), color="green")

    # Streak Status and Milestones
    st.subheader("Streak Status 🔥")
    st.write(f"Current Streak: {user_data['streak_count']} day(s)")
    st.write("Achieved Milestones: " + ", ".join(map(str, user_data["milestones"])))

    # Breakdown of Carbon Savings by Category
    st.subheader("Breakdown of Carbon Savings by Category")
    category_df = pd.DataFrame(user_data["savings_by_category"].items(), columns=["Category", "Savings (kg)"])
    st.bar_chart(category_df.set_index("Category"), color="green")

    # Comparison with Regional/Global Averages
    st.subheader("Comparison with Averages ")
    st.write(f"Your Total CO₂ Savings: {user_data['monthly_savings']} kg")
    st.write(f"Regional Average: {user_data['regional_average']} kg")
    st.write(f"Global Average: {user_data['global_average']} kg")

    # Visual comparison
    fig, ax = plt.subplots()
    averages = [user_data['monthly_savings'], user_data['regional_average'], user_data['global_average']]
    labels = ['Your Savings', 'Regional Average', 'Global Average']
    ax.bar(labels, averages, color=['#228B22', '#3CB371', '#98FB98'])
    ax.set_ylabel('CO₂ Savings (kg)')
    ax.set_title('Comparison of CO₂ Savings')
    st.pyplot(fig)

# Main function for the Personal Dashboard
def personal_dashboard():
    display_personal_dashboard()

