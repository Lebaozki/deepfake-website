import streamlit as st
#Malvina having fun with git and loving it!


# Set page title and favicon
st.set_page_config(
    page_title="Deepfake Detection",
    page_icon=":smiley:",
)

# Define Streamlit app content
st.title("Deepfake Detection")

# Subheading
st.subheader("Is your image real?")

url = 'https://deepfakepreproc-abexurulqa-ew.a.run.app/docs'

# File upload widget
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Display uploaded image if available
if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

# Prediction result section
st.markdown("### Prediction Result")
st.write("Predicted result will appear here after uploading an image.")

# Disclaimer
st.markdown("## Disclaimer")
st.write(
    "This project is an academic endeavor. While the results of our predictive model are impressive, we are not the definitive tool to prove anything. Please use it with caution and discretion."
)

# Add any additional content or styling as needed
#Test commit
