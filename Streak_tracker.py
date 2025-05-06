import streamlit as st
from datetime import datetime, timedelta
import random
import pandas as pd

# Generate expanded user dataset with streak history
def generate_users(n=30):
    regions = ['Trivandrum', 'Kollam', 'Kochi', 'Alappuzha', 'Global']
    teams = ['GreenWizards', 'EcoStars', 'PlanetSavers', 'CarbonCutters']
    users = {}

    for i in range(n):
        username = f"User{i+1}"
        start_date = datetime.now().date() - timedelta(days=6)
        streak_history = [random.randint(0, 1) for _ in range(7)]
        users[username] = {
            "user_id": username,
            "total_co2_saved": random.randint(10, 150),
            "region": random.choice(regions),
            "team": random.choice(teams),
            "streak_count": sum(streak_history),
            "last_action_date": datetime.now().date() - timedelta(days=random.randint(0, 3)),
            "milestones": [5, 10, 15],
            "badges": [],
            "streak_history": streak_history,
            "history_dates": [start_date + timedelta(days=i) for i in range(7)]
        }
    return users

# Simulated in-memory user data
users = generate_users(30)

def update_streak(user):
    current_date = datetime.now().date()
    last_action_date = user["last_action_date"]

    if last_action_date is None:
        user["streak_count"] = 1
    else:
        diff = (current_date - last_action_date).days
        if diff == 1:
            user["streak_count"] += 1
        elif diff > 1:
            user["streak_count"] = 1

    user["last_action_date"] = current_date

    # Update streak history
    user["streak_history"].pop(0)
    user["streak_history"].append(1)
    user["history_dates"].pop(0)
    user["history_dates"].append(current_date)

    check_milestones(user)
    return user["streak_count"]

def check_milestones(user):
    for milestone in user["milestones"]:
        if user["streak_count"] == milestone and milestone not in user["badges"]:
            user["badges"].append(milestone)
            st.success(f"🎉 {user['user_id']} reached a streak of {milestone} days and earned a badge!")

def display_streak(user):
    st.markdown(f"## {user['user_id']}")
    st.markdown(f"""<div style='font-size:28px; font-weight:bold; color:green;'>🔥 Current Streak: {user['streak_count']} day(s)</div>""", unsafe_allow_html=True)
    if user['last_action_date']:
        st.write(f"📅 Last Action Date: {user['last_action_date'].strftime('%Y-%m-%d')}")

    # Streak history line chart
    streak_df = pd.DataFrame({
        "Date": user["history_dates"],
        "Streak": user["streak_history"]
    }).set_index("Date")
    
    st.subheader("📈 Weekly Streak History")
    st.line_chart(streak_df)

    if user["badges"]:
        st.markdown("🏅 **Badges Earned:**")
        st.write(", ".join([f"{badge} days" for badge in user["badges"]]))

def streak_tracker():
    st.title("🌏 Eco Action Streak Tracker")

    user_list = list(users.keys())
    selected_user = st.selectbox("Select a user", user_list)

    user = users[selected_user]

    if st.button("Record Eco-Friendly Action"):
        updated_streak = update_streak(user)
        st.success(f"Action recorded! {selected_user}'s current streak is {updated_streak} day(s).")

    display_streak(user)

# Run the streak tracker
if __name__ == "__main__":
    streak_tracker()
