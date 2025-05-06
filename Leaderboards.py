import streamlit as st
import pandas as pd
import random

# Generate larger simulated user data
def generate_users(n=50):
    regions = ['Trivandrum', 'Kollam', 'Kochi', 'Global']
    teams = ['GreenWizards', 'EcoStars', 'PlanetSavers', 'CarbonCutters']
    users = []

    for i in range(n):
        user = {
            "username": f"User{i+1}",
            "total_co2_saved": random.randint(10, 100),
            "streak_count": random.randint(1, 30),
            "region": random.choice(regions),
            "team": random.choice(teams),
            "friends": random.sample([f"User{j+1}" for j in range(n) if j != i], 5)  # simulate 5 friends
        }
        users.append(user)
    return users

user_data = generate_users(50)

def display_leaderboard(filter_option, current_user='User1'):
    df = pd.DataFrame(user_data)

    if filter_option == "Global":
        filtered_df = df

    elif filter_option == "Regional":
        region = st.selectbox("Select your region", sorted(df['region'].unique()))
        filtered_df = df[df['region'] == region]

    elif filter_option == "Friends":
        # Find friends of current user
        user_row = next((u for u in user_data if u['username'] == current_user), None)
        if user_row:
            friend_list = user_row['friends']
            filtered_df = df[df['username'].isin(friend_list + [current_user])]
        else:
            st.warning("User not found!")
            return

    elif filter_option == "Corporate Teams":
        team = st.selectbox("Select your corporate team", sorted(df['team'].unique()))
        filtered_df = df[df['team'] == team]

    # Sort by total CO₂ saved
    filtered_df = filtered_df.sort_values(by="total_co2_saved", ascending=False).reset_index(drop=True)
    filtered_df.insert(0, 'Rank', range(1, len(filtered_df) + 1))

    # Display leaderboard
    st.write("### Leaderboard")
    st.dataframe(filtered_df[['Rank', 'username', 'total_co2_saved', 'streak_count']])

    # Gamification highlights
    top_streak_holder = filtered_df.loc[filtered_df['streak_count'].idxmax()]
    st.write(f"🏆 **Top Streak Holder:** {top_streak_holder['username']} with a streak of {top_streak_holder['streak_count']} days!")

    greenest_user = filtered_df.loc[filtered_df['total_co2_saved'].idxmax()]
    st.write(f"🌱 **Greenest User of the Month:** {greenest_user['username']} with {greenest_user['total_co2_saved']} kg CO₂ saved!")

# Main Leaderboard App
def leaderboard():
    st.title("🌍 EcoSnap Leaderboard: Compete and Motivate")

    filter_option = st.selectbox("Select Leaderboard Filter", ["Global", "Regional", "Friends", "Corporate Teams"])
    if st.button("Show Leaderboard"):
        display_leaderboard(filter_option)

# Run the app
if __name__ == "__main__":
    leaderboard()
