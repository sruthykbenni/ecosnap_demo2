import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image
import io

# Load the TensorFlow Lite model
def load_model(model_path):
    interpreter = tf.lite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()
    return interpreter

# Function to classify the image
def classify_image(interpreter, image):
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # Preprocess the image
    image = image.resize((224, 224))  # Resize to model input size
    input_data = np.array(image) / 255.0  # Normalize
    input_data = np.expand_dims(input_data, axis=0).astype(np.float32)

    # Run inference
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])

    # Get the predicted class and confidence
    predicted_class = np.argmax(output_data[0])
    confidence_score = output_data[0][predicted_class]
    return predicted_class, confidence_score

# Function to display classification results
def display_classification_results(predicted_class, confidence_score):
    categories = [
        "Reusable shopping bags",
        "Cloth over plastic packaging",
        "Bicycle use vs. car travel",
        "Tree planting events",
        "Use of public transit",
        "Zero waste or composting activities"
    ]
    
    st.write("### Classification Results")
    st.write(f"Predicted Action: {categories[predicted_class]}")
    st.write(f"Confidence Score: {confidence_score:.2f}")

    # Allow user to correct classification
    correction = st.selectbox("Is this classification correct?", ["Yes", "No"])
    if correction == "No":
        st.write("Please provide the correct action:")
        correct_action = st.selectbox("Correct Action", categories)
        st.write(f"Corrected Action: {correct_action}")
        # Here you would implement logic to store the correction for future training
        st.success("Thank you for your feedback! This will help improve the model.")

# Main function for the AI Analyzer
def ai_analyzer():
    st.title("AI Analyzer: Classify Your Eco-Friendly Action")
    
    # Load the TensorFlow Lite model
    model_path = "path/to/your/model.tflite"  # Update with your model path
    interpreter = load_model(model_path)

    # File uploader for image input
    uploaded_file = st.file_uploader("Upload an image of your eco-friendly action", type=['png', 'jpg', 'jpeg'])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        if st.button("Analyze Image"):
            predicted_class, confidence_score = classify_image(interpreter, image)
            display_classification_results(predicted_class, confidence_score)
