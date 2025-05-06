import streamlit as st
from datetime import datetime

# Unified user data structure
user_data = {
    "user_id": "user123",
    "total_co2_saved": 52.3,  # Total CO₂ saved
    "available_rewards": [],
    "redeemed_rewards": [],
    "streak_count": 7,
    "last_action_date": datetime.now().date(),
    "milestones": [5, 10, 15],
    "badges": [5],
    "history_dates": [datetime(2024, 4, 29).date(), datetime(2024, 4, 30).date(),
                      datetime(2024, 5, 1).date(), datetime(2024, 5, 2).date(),
                      datetime(2024, 5, 3).date(), datetime(2024, 5, 4).date(),
                      datetime(2024, 5, 5).date()],
    "streak_history": [1, 2, 3, 4, 5, 6, 7]
}

# Predefined CO₂ milestones and corresponding rewards
REWARD_MILESTONES = {
    5: "5% Discount Voucher for Eco Products",
    10: "Coupon from Partner Brand",
    30: "Tree Planting Credit",
    50: "Digital Certificate of Green Achievement"
}

def update_rewards(user):
    """
    Check user's CO2 savings and update available rewards based on milestones.
    """
    for milestone, reward in REWARD_MILESTONES.items():
        if user["total_co2_saved"] >= milestone and reward not in user["available_rewards"] and reward not in user["redeemed_rewards"]:
            user["available_rewards"].append(reward)

def get_next_milestone(co2_saved):
    """
    Get the next CO2 milestone the user is working toward.
    """
    upcoming = sorted([m for m in REWARD_MILESTONES if m > co2_saved])
    return upcoming[0] if upcoming else None

def reward_center():
    st.title("🎁 Reward Center: Earn and Redeem Your Green Rewards")

    # Update rewards based on total CO2 saved
    update_rewards(user_data)

    st.markdown(f"**User ID:** {user_data['user_id']}")
    st.metric(label="🌱 Total CO₂ Saved", value=f"{user_data['total_co2_saved']:.2f} kg")

    # Progress bar to next milestone
    next_milestone = get_next_milestone(user_data["total_co2_saved"])
    if next_milestone:
        progress = user_data["total_co2_saved"] / next_milestone
        st.subheader(f"📊 Progress to Next Reward ({next_milestone} kg)")
        st.progress(min(progress, 1.0))
    else:
        st.success("🎉 You've achieved all available rewards!")

    # Display available rewards
    st.subheader("🎯 Available Rewards")
    if user_data["available_rewards"]:
        for reward in user_data["available_rewards"]:
            st.write(f"🟢 {reward}")
    else:
        st.write("No rewards available yet. Keep reducing your carbon footprint!")

    # Redeem reward
    if user_data["available_rewards"]:
        reward_to_redeem = st.selectbox("Select a reward to redeem", user_data["available_rewards"])
        if st.button("Redeem Reward"):
            user_data["available_rewards"].remove(reward_to_redeem)
            user_data["redeemed_rewards"].append(reward_to_redeem)
            st.success(f"✅ Reward '{reward_to_redeem}' redeemed successfully!")

    # Display redeemed rewards
    st.subheader("🎉 Redeemed Rewards")
    if user_data["redeemed_rewards"]:
        for reward in user_data["redeemed_rewards"]:
            st.write(f"✔️ {reward}")
    else:
        st.write("You haven't redeemed any rewards yet.")

    # Notify user if new rewards are available
    if user_data["available_rewards"]:
        st.info("🎊 You've unlocked new rewards! Claim them now!")

# Main function for the CSR Dashboard
def csr_dashboard():
    display_csr_dashboard()
