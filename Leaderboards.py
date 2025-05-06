import streamlit as st
import pandas as pd
import random

# Simulate user data
def generate_users(n=50):
    regions = ['Trivandrum', 'Kollam', 'Kochi', 'Global']
    teams = ['GreenWizards', 'EcoStars', 'PlanetSavers', 'CarbonCutters']
    users = []

    for i in range(n):
        username = f"User{i+1}"
        user = {
            "username": username,
            "total_co2_saved": random.randint(10, 100),
            "streak_count": random.randint(1, 30),
            "region": random.choice(regions),
            "team": random.choice(teams),
            "friends": random.sample([f"User{j+1}" for j in range(n) if j != i], 5)
        }
        users.append(user)
    return users

user_data = generate_users(50)
df = pd.DataFrame(user_data)

def display_leaderboard(filtered_df):
    filtered_df = filtered_df.sort_values(by="total_co2_saved", ascending=False).reset_index(drop=True)
    filtered_df.insert(0, 'Rank', range(1, len(filtered_df) + 1))

    st.write("### Leaderboard")
    st.dataframe(filtered_df[['Rank', 'username', 'total_co2_saved', 'streak_count']])

    if not filtered_df.empty:
        top_streak_holder = filtered_df.loc[filtered_df['streak_count'].idxmax()]
        st.write(f"🏆 **Top Streak Holder:** {top_streak_holder['username']} with a streak of {top_streak_holder['streak_count']} days!")

        greenest_user = filtered_df.loc[filtered_df['total_co2_saved'].idxmax()]
        st.write(f"🌱 **Greenest User of the Month:** {greenest_user['username']} with {greenest_user['total_co2_saved']} kg CO₂ saved!")
    else:
        st.warning("No users found for the selected filter.")

def leaderboard():
    st.title("🌍 EcoSnap Leaderboard: Compete and Motivate")

    filter_option = st.selectbox("Select Leaderboard Filter", ["Global", "Regional", "Friends", "Corporate Teams"])
    current_user = st.selectbox("Select your username", df['username'].unique())

    if filter_option == "Global":
        filtered_df = df

    elif filter_option == "Regional":
        user_region = df[df['username'] == current_user]['region'].values[0]
        st.info(f"Showing leaderboard for your region: **{user_region}**")
        filtered_df = df[df['region'] == user_region]

    elif filter_option == "Friends":
        user_friends = df[df['username'] == current_user]['friends'].values[0]
        filtered_df = df[df['username'].isin(user_friends + [current_user])]

    elif filter_option == "Corporate Teams":
        user_team = df[df['username'] == current_user]['team'].values[0]
        st.info(f"Showing leaderboard for your team: **{user_team}**")
        filtered_df = df[df['team'] == user_team]

    display_leaderboard(filtered_df)

# Run the app
if __name__ == "__main__":
    leaderboard()
