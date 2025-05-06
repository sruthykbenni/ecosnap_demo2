import streamlit as st

# CO₂ savings data based on actions
CO2_SAVINGS = {
    "Bicycle": 0.75,  # kg CO₂ saved per 3 km
    "Public Transport": 0.5,  # kg CO₂ saved per trip
    "Reusable Bags": 0.1,  # kg CO₂ saved per bag
    "Composting": 0.2,  # kg CO₂ saved per composting action
    "Tree Planting": 1.0,  # kg CO₂ saved per tree planted
    "Cloth Over Plastic": 0.05  # kg CO₂ saved per use
}

def estimate_co2(action, distance=None):
    """
    Estimate CO₂ savings based on the action and distance.
    
    Parameters:
    - action (str): The type of eco-friendly action.
    - distance (float): The distance for actions that require it (e.g., bicycle, public transport).
    
    Returns:
    - float: Estimated CO₂ savings.
    """
    if action not in CO2_SAVINGS:
        return 0.0

    if action in ["Bicycle", "Public Transport"] and distance is not None:
        # For bicycle and public transport, scale savings based on distance
        if action == "Bicycle":
            return CO2_SAVINGS[action] * (distance / 3)  # Adjust based on distance
        elif action == "Public Transport":
            return CO2_SAVINGS[action] * distance  # Assume distance is in trips
    else:
        return CO2_SAVINGS[action]  # Return standard savings for other actions

def display_co2_estimation(action, distance):
    """
    Display the estimated CO₂ savings to the user.
    
    Parameters:
    - action (str): The type of eco-friendly action.
    - distance (float): The distance for actions that require it.
    """
    estimated_savings = estimate_co2(action, distance)
    st.write(f"Estimated CO₂ Savings for {action}: {estimated_savings:.2f} kg 🤝")

# Main function for the CO₂ Estimator
def co2_estimator():
    st.title("🌏 CO₂ Savings Estimator")

    # Select action type
    action = st.selectbox("Select your eco-friendly action", list(CO2_SAVINGS.keys()))

    # Input distance for actions that require it
    distance = None
    if action in ["Bicycle", "Public Transport"]:
        distance = st.number_input("Enter distance (in km)", min_value=0.0, step=0.1)

    if st.button("Estimate CO₂ Savings"):
        display_co2_estimation(action, distance)
