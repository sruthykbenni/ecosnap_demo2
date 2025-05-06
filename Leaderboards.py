import streamlit as st
import pandas as pd

# Simulated user data for demonstration
user_data = [
    {"Username": "EcoWarrior", "Total Co2 saved": 50, "Streak count": 10, "Region": "Global"},
    {"Username": "GreenThumb", "Total Co2 saved": 40, "Streak count": 5, "Region": "Trivandrun"},
    {"Username": "SustainableSam", "Total Co2 saved": 30, "Streak count": 15, "Region": "Kollam"},
    {"Username": "PlanetProtector", "Total Co2 saved": 25, "Streak count": 7, "Region": "Kollam"},
    {"Username": "EcoFriendly", "Total Co2 saved": 20, "Streak count": 3, "Region": "Global"},
    {"Username": "TreeHugger", "Total Co2 saved": 15, "Streak count": 12, "Region": "Trivandrum"},
]

def display_leaderboard(filter_option):
    """
    Display the leaderboard based on the selected filter option.
    
    Parameters:
    - filter_option (str): The selected filter for the leaderboard.
    """
    # Convert user data to DataFrame for easier manipulation
    df = pd.DataFrame(user_data)

    # Filter based on the selected option
    if filter_option == "Global":
        filtered_df = df
    elif filter_option == "Regional":
        region = st.selectbox("Select your region", df['Region'].unique())
        filtered_df = df[df['Region'] == region]
    elif filter_option == "Friends":
        filtered_df = df  # Replace with actual friends filter logic
    elif filter_option == "Corporate Teams":
        filtered_df = df  # Replace with actual corporate team logic

    # Sort by total CO₂ saved
    filtered_df = filtered_df.sort_values(by="total_co2_saved", ascending=False).reset_index(drop=True)

    # Add Rank column starting from 1
    filtered_df.insert(0, 'Rank', range(1, len(filtered_df) + 1))

    # Display the leaderboard
    st.write("### Leaderboard")
    st.dataframe(filtered_df[['Rank', 'Username', 'Total Co2 saved', 'Streak count']])

    # Highlight gamified metrics
    top_streak_holder = filtered_df.loc[filtered_df['streak_count'].idxmax()]
    st.write(f"🏆 **Top Streak Holder:** {top_streak_holder['Username']} with a streak of {top_streak_holder['Streak count']} days!")

    greenest_user = filtered_df.loc[filtered_df['total_co2_saved'].idxmax()]
    st.write(f"🌱 **Greenest User of the Month:** {greenest_user['Username']} with {greenest_user['Total Co2 saved']} kg CO₂ saved!")


# Main function for the Leaderboard
def leaderboard():
    st.title("Leaderboard: Compete and Motivate")

    filter_option = st.selectbox("Select Leaderboard Filter", ["Global", "Regional", "Friends", "Corporate Teams"])
    
    if st.button("Show Leaderboard"):
        display_leaderboard(filter_option)
