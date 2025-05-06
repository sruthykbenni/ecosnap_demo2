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

# Page mapping
PAGES = {
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
    
    # Use session state to track the current page
    if 'page' not in st.session_state:
        st.session_state.page = "Home"

    # Navigation UI
    st.title("🌿 EcoSnap Navigation")
    
    if st.session_state.page == "Home":
        st.markdown("### Select a feature to explore:")
        for page_name in PAGES:
            if st.button(page_name):
                st.session_state.page = page_name
                st.experimental_rerun()

        st.markdown("---")
        st.markdown("""
        **EcoSnap** is your eco-friendly tracking app! 🌍  
        Take action, track your savings, earn rewards, and compete on the leaderboard! 💚
        """)
    
    else:
        # Show selected feature
        if st.button("🔙 Go Back to Home"):
            st.session_state.page = "Home"
            st.experimental_rerun()
        
        PAGES[st.session_state.page]()  # Call the function

if __name__ == "__main__":
    main()
