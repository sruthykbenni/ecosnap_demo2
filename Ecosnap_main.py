import streamlit as st

# Import all module functions
from AI_analyzer import ai_analyzer
from CSR_dashboard import csr_dashboard
from Co2_estimator import co2_estimator
from Eco_snap_camera import eco_snap_camera
from Leaderboards import leaderboards
from Personal_dashboard import personal_dashboard
from Reward_center import reward_center
from Streak_tracker import streak_tracker

# Sidebar Navigation with emojis
PAGES = {
    "🏠 Home": "home",
    "📷 EcoSnap Camera": eco_snap_camera,
    "📊 CO₂ Estimator": co2_estimator,
    "🧠 AI Analyzer": ai_analyzer,
    "📈 Personal Dashboard": personal_dashboard,
    "🏆 Leaderboards": leaderboards,
    "🎁 Reward Center": reward_center,
    "🔥 Streak Tracker": streak_tracker,
    "🌱 CSR Dashboard": csr_dashboard
}

def main():
    st.set_page_config(page_title="EcoSnap 🌍", layout="wide")
    st.sidebar.title("🌿 EcoSnap Navigation")
    selection = st.sidebar.radio("Choose a feature:", list(PAGES.keys()))

    if selection == "🏠 Home":
        st.title("🌎 Welcome to EcoSnap!")
        st.markdown("Make your eco-friendly actions count! 🌱\n\nChoose a feature from the left panel to get started.")
        st.image("https://images.unsplash.com/photo-1501004318641-b39e6451bec6", use_column_width=True)
    else:
        PAGES[selection]()  # Call the selected function

if __name__ == "__main__":
    main()
