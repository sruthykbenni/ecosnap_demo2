import streamlit as st
from AI_analyzer import AI_analyzer
from CSR_dashboard import CSR_dashboard
from CO2_estimator import CO2_estimator
from Eco_snap_camera import Eco_snap_camera
from Leaderboards import Leaderboards
from Personal_dashboard import Personal_dashboard
from Reward_center import Reward_center
from Streak_tracker import Streak_tracker

# Main function to display the app
def main():
    st.set_page_config(page_title="EcoSnap App", page_icon="🌍", layout="wide")
    
    # App title
    st.title("Welcome to EcoSnap 🌱")
    st.markdown("""
        **EcoSnap** is your eco-friendly tracking app! 🌍  
        Take action, track your savings, earn rewards, and compete on the leaderboard! 🌿
    """)

    # Sidebar navigation
    st.sidebar.title("Navigation 🧭")
    choice = st.sidebar.radio("Choose a Feature", [
        "🏠 Home", 
        "🤖 AI Analyzer", 
        "📊 CSR Dashboard", 
        "🌍 CO2 Estimator", 
        "📸 Eco Snap Camera", 
        "🏆 Leaderboards", 
        "📊 Personal Dashboard", 
        "🎁 Reward Center", 
        "🔥 Streak Tracker"
    ])

   # Home Page
    if choice == "🏠 Home":
        st.subheader("Welcome to EcoSnap!")
        st.markdown("This app helps you track your eco-friendly actions, estimate CO2 savings, and stay motivated to make a positive impact on the planet. 🌍 Explore the different features to learn more about your eco contributions! 🌱")
    
    # AI Analyzer Page
    elif choice == "🤖 AI Analyzer":
        AI_analyzer()

    # CSR Dashboard Page
    elif choice == "📊 CSR Dashboard":
        CSR_dashboard()

    # CO2 Estimator Page
    elif choice == "🌍 CO2 Estimator":
        CO2_estimator()

    # Eco Snap Camera Page
    elif choice == "📸 Eco Snap Camera":
        Eco_snap_camera()

    # Leaderboards Page
    elif choice == "🏆 Leaderboards":
        Leaderboards()

    # Personal Dashboard Page
    elif choice == "📊 Personal Dashboard":
        Personal_dashboard()

    # Reward Center Page
    elif choice == "🎁 Reward Center":
        Reward_center()

    # Streak Tracker Page
    elif choice == "🔥 Streak Tracker":
        Streak_tracker()
# Run the main function
if __name__ == "__main__":
    main()
