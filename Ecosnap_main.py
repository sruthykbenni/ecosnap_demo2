import streamlit as st

# Import all module functions
from AI_analyzer import ai_analyzer
from CSR_dashboard import csr_dashboard
from Co2_estimator import co2_estimator
from Ecosnap_camera import ecosnap_camera
from Leaderboards import leaderboard
from Personal_dashboard import personal_dashboard
from Reward_center import reward_center
from Streak_tracker import streak_tracker

# Sidebar Navigation with emojis
PAGES = {
    "🏠 Home": "home",
    "📷 EcoSnap Camera": ecosnap_camera,
    "📊 CO₂ Estimator": co2_estimator,
    "🧠 AI Analyzer": ai_analyzer,
    "📈 Personal Dashboard": personal_dashboard,
    "🏆 Leaderboards": leaderboard,
    "🎁 Reward Center": reward_center,
    "🔥 Streak Tracker": streak_tracker,
    "🌱 CSR Dashboard": csr_dashboard
}

def main():
    st.set_page_config(page_title="EcoSnap 🌍", layout="wide")
    st.sidebar.title("🌿 EcoSnap Navigation")
    selection = st.sidebar.radio("Choose a feature:", list(PAGES.keys()))

    if selection == "🏠 Home":
    st.title("Welcome to EcoSnap 🌱")
    st.markdown("""
        **EcoSnap** is your eco-friendly tracking app! 🌍  
        Take action, track your savings, earn rewards, and compete on the leaderboard! 💚
    """)

    else:
        PAGES[selection]()  # Call the selected function

if __name__ == "__main__":
    main()
