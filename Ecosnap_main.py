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

# Home page display function
def show_home():
    st.title("Welcome to EcoSnap 🌱")
    st.markdown("""
    **EcoSnap** is your eco-friendly tracking app! 🌍  
    Take action, track your savings, earn rewards, and compete on the leaderboard! 💚
    """)

# Sidebar Navigation with emojis
PAGES = {
    "🌏 Home": show_home,
    "📷 EcoSnap Camera": ecosnap_camera,
    "📊 CO₂ Estimator": co2_estimator,
    "📈 Personal Dashboard": personal_dashboard,
    "🏆 Leaderboards": leaderboard,
    "🔥 Streak Tracker": streak_tracker,
    "🌱 CSR Dashboard": csr_dashboard,
    "⭐ Reward Center": reward_center,
    "🧩 AI Analyzer": ai_analyzer
}

def main():
    st.set_page_config(page_title="EcoSnap 🌍", layout="wide")
    st.sidebar.title("🌿 EcoSnap Navigation")

    # Determine selected feature based on button clicked
    selected_feature = None
    for name in PAGES.keys():
        if st.sidebar.button(name):
            selected_feature = name
            break

    if selected_feature is None:
        show_home()
    else:
        PAGES[selected_feature]()  # Call the selected function safely

if __name__ == "__main__":
    main()
