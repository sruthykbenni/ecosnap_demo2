import streamlit as st
from datetime import datetime
from PIL import Image
import io
from geopy.geocoders import Nominatim

# Function to get location from user input
def get_location():
    geolocator = Nominatim(user_agent="eco_snap")
    location_input = st.text_input("Enter your location (e.g., City, Country):")
    if location_input:
        location = geolocator.geocode(location_input)
        if location:
            return f"{location.latitude}, {location.longitude}"
        else:
            st.warning("Location not found. Please enter a valid location.")
    return None

# EcoSnap Camera Feature
def ecosnap_camera():
    st.title("EcoSnap Camera 📷")
    st.markdown("""
    ### Capture Your Eco-Friendly Action 
    Please upload an image of your eco-friendly action (e.g., using public transport, carrying reusable items, cycling, composting, or participating in tree planting drives).
    """)

    # File uploader simulating camera capture in browser
    uploaded_file = st.file_uploader("Upload an image of your eco-friendly action", type=['png', 'jpg', 'jpeg'])

    # Location input (simulating optional metadata)
    location = get_location()

    # Display timestamp automatically
    timestamp = datetime.now()
    st.write(f"Timestamp (capture time): {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")

    if uploaded_file is not None:
        # Display uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)


        # Simulate submit button for upload
        if st.button("Submit Eco-Friendly Action"):
            # Here backend upload and processing would happen
            st.success("Image and metadata submitted successfully! ✅")
            st.json({
                "filename": uploaded_file.name,
                "timestamp": timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                "location": location if location else "Not provided"
            })
    else:
        st.info("Please upload an image to continue.")

# Run the EcoSnap Camera feature
if __name__ == "__main__":
    ecosnap_camera()
