import streamlit as st
import random
from datetime import datetime, timedelta

# Generate larger simulated user data
def generate_users(n=50):
    regions = ['Trivandrum', 'Kollam', 'Kochi', 'Global']
    teams = ['GreenWizards', 'EcoStars', 'PlanetSavers', 'CarbonCutters']
    users = []

    for i in range(n):
        username = f"User{i+1}"
        streak = random.randint(3, 15)
        today = datetime.now().date()
        history = [today - timedelta(days=x) for x in reversed(range(streak))]

        user = {
            "user_id": username,
            "total_co2_saved": random.randint(10, 100),
            "available_rewards": [],
            "redeemed_rewards": [],
            "streak_count": streak,
            "last_action_date": today,
            "milestones": [5, 10, 30, 50],
            "badges": [5] if random.random() > 0.5 else [],
            "history_dates": history,
            "streak_history": list(range(1, streak + 1)),
            "region": random.choice(regions),
            "team": random.choice(teams),
            "friends": random.sample([f"User{j+1}" for j in range(n) if j != i], 5)
        }
        users.append(user)
    return users

# Predefined CO₂ milestones and corresponding rewards
REWARD_MILESTONES = {
    5: "5% Discount Voucher for Eco Products",
    10: "Coupon from Partner Brand",
    30: "Tree Planting Credit",
    50: "Digital Certificate of Green Achievement"
}

# Reward updating logic
def update_rewards(user):
    for milestone, reward in REWARD_MILESTONES.items():
        if (user["total_co2_saved"] >= milestone and
            reward not in user["available_rewards"] and
            reward not in user["redeemed_rewards"]):
            user["available_rewards"].append(reward)

def get_next_milestone(co2_saved):
    upcoming = sorted([m for m in REWARD_MILESTONES if m > co2_saved])
    return upcoming[0] if upcoming else None

# Reward center view
def reward_center(selected_user):
    st.title("🎁 Reward Center: Earn and Redeem Your Green Rewards")

    update_rewards(selected_user)

    st.markdown(f"**User ID:** `{selected_user['user_id']}`")
    st.metric(label="🌱 Total CO₂ Saved", value=f"{selected_user['total_co2_saved']:.2f} kg")

    # Progress bar to next milestone
    next_milestone = get_next_milestone(selected_user["total_co2_saved"])
    if next_milestone:
        progress = selected_user["total_co2_saved"] / next_milestone
        st.subheader(f"📈 Progress to Next Reward ({next_milestone} kg)")
        st.progress(min(progress, 1.0))
    else:
        st.success("🎉 You've achieved all available rewards!")

    # Display available rewards
    st.subheader("🎯 Available Rewards")
    if selected_user["available_rewards"]:
        for reward in selected_user["available_rewards"]:
            st.write(f"🌟 {reward}")
    else:
        st.write("No rewards available yet. Keep reducing your carbon footprint!")

    # Redeem reward
    if selected_user["available_rewards"]:
        reward_to_redeem = st.selectbox("Select a reward to redeem", selected_user["available_rewards"])
        if st.button("Redeem Reward"):
            selected_user["available_rewards"].remove(reward_to_redeem)
            selected_user["redeemed_rewards"].append(reward_to_redeem)
            st.success(f"✅ Reward '{reward_to_redeem}' redeemed successfully!")

    # Display redeemed rewards
    st.subheader("🎉 Redeemed Rewards")
    if selected_user["redeemed_rewards"]:
        for reward in selected_user["redeemed_rewards"]:
            st.write(f"✔️ {reward}")
    else:
        st.write("You haven't redeemed any rewards yet.")

    # Notify user if new rewards are available
    if selected_user["available_rewards"]:
        st.info("🎊 You've unlocked new rewards! Claim them now!")

# Main Streamlit app
def main():
    all_users = generate_users(50)

    st.sidebar.header("🔎 Select User")
    user_ids = [user["user_id"] for user in all_users]
    selected_id = st.sidebar.selectbox("Choose a User ID", user_ids)

    # Find selected user from the list
    selected_user = next((u for u in all_users if u["user_id"] == selected_id), None)

    if selected_user:
        reward_center(selected_user)
    else:
        st.error("User not found!")

if __name__ == "__main__":
    main()
