import streamlit as st
from datetime import datetime, timedelta
import random
import pandas as pd
import altair as alt

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
    st.header(user['user_id'])

    st.subheader("🔥 Current Streak")
    st.success(f"{user['streak_count']} day(s)")

    if user['last_action_date']:
        st.write(f"📅 Last Action Date: {user['last_action_date'].strftime('%Y-%m-%d')}")

    # Streak history chart with sorted data and milestone markers
    if user.get("history_dates") and user.get("streak_history"):
        # Create DataFrame and sort chronologically
        streak_df = pd.DataFrame({
            "Date": user["history_dates"],
            "Streak": user["streak_history"]
        })
        streak_df["Date"] = pd.to_datetime(streak_df["Date"])
        streak_df = streak_df.sort_values("Date")

        # Altair line chart with milestone annotations
        base = alt.Chart(streak_df).mark_line(point=True).encode(
            x='Date:T',
            y='Streak:Q',
            tooltip=['Date:T', 'Streak:Q']
        ).properties(title="📈 Weekly Streak History")

        milestones = [m for m in user["milestones"] if m in user["streak_history"]]
        milestone_df = streak_df[streak_df["Streak"].isin(milestones)]

        if not milestone_df.empty:
            milestone_points = alt.Chart(milestone_df).mark_point(color='orange', size=100).encode(
                x='Date:T',
                y='Streak:Q',
                tooltip=alt.Tooltip('Streak:Q', title='Milestone Badge')
            )
            chart = base + milestone_points
        else:
            chart = base

        st.altair_chart(chart, use_container_width=True)

    # Badges earned
    if user["badges"]:
        st.subheader("🏅 Badges Earned")
        for badge in sorted(user["badges"]):
            st.markdown(f"- **{badge} days** badge")

def streak_tracker():
    st.title("🌎 Eco Action Streak Tracker")

    user_list = list(users.keys())
    selected_user = st.selectbox("Select a user", user_list)

    user = users[selected_user]

    display_streak(user)

# Run the streak tracker
if __name__ == "__main__":
    streak_tracker()
