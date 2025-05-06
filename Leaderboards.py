import streamlit as st
import pandas as pd
import random

# Generate realistic user data
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
            "team": random.choice(teams)
        }
        users.append(user)

    return users

# Fake friend mapping for demonstration
friend_map = {
    "User1": ["User2", "User3", "User10"],
    "User2": ["User1", "User4", "User5"],
    "User3": ["User1", "User6"],
    "User4": ["User2", "User5"],
    "User5": ["User2", "User4", "User6"]
}

# Data
user_data = generate_users(50)
df = pd.DataFrame(user_data)

def display_leaderboard(filtered_df):
    filtered_df = filtered_df.sort_values(by="total_co2_saved", ascending=False).reset_index(drop=True)
    filtered_df.insert(0, 'Rank', range(1, len(filtered_df) + 1))

    st.write("### Leaderboard")
    st.dataframe(filtered_df[['Rank', 'username', 'total_co2_saved', 'streak_count']])

    if not filtered_df.empty:
        top_streak = filtered_df.loc[filtered_df['streak_count'].idxmax()]
        top_green = filtered_df.loc[filtered_df['total_co2_saved'].idxmax()]
        st.success(f"🏆 Top Streak: {top_streak['username']} - {top_streak['streak_count']} days")
        st.info(f"🌱 Greenest User: {top_green['username']} - {top_green['total_co2_saved']} kg CO₂ saved")
    else:
        st.warning("No users found for this filter.")

def leaderboard():
    st.title("🌍 EcoSnap Leaderboard")

    filter_option = st.selectbox("Select Leaderboard Filter", ["Global", "Regional", "Friends", "Corporate Teams"])

    filtered_df = df.copy()

    if filter_option == "Regional":
        selected_region = st.selectbox("Choose Region", sorted(df['region'].unique()))
        filtered_df = df[df['region'] == selected_region]

    elif filter_option == "Corporate Teams":
        selected_team = st.selectbox("Choose Corporate Team", sorted(df['team'].unique()))
        filtered_df = df[df['team'] == selected_team]

    elif filter_option == "Friends":
        selected_user = st.selectbox("Choose Your Username", sorted(df['username'].unique()))
        friend_list = friend_map.get(selected_user, [])
        friend_list.append(selected_user)  # include self
        filtered_df = df[df['username'].isin(friend_list)]

    # Global doesn't need filtering

    if st.button("Show Leaderboard"):
        display_leaderboard(filtered_df)

# Run the app
if __name__ == "__main__":
    leaderboard()
