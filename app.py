import streamlit as st
import streamlit as st
import requests
from PIL import Image
from io import BytesIO

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
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Check if an image is uploaded
if uploaded_image:
    st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

    # Make an API request when a button is clicked
    if st.button("Get Prediction"):
        # API endpoint URL
        api_url = "https://deepfakepreproc-abexurulqa-ew.a.run.app/upload_image"  # Replace with your API URL

        try:
            # Prepare the image for API request
            image_data = BytesIO(uploaded_image.read())
            files = {"image": ("image.jpg", image_data)}

            # Send the image to the API as a POST request
            response = requests.post(api_url, data=files)

            if response.status_code == 200:
                # Parse the API response (assuming it's JSON)
                prediction = response.json()
                st.write("Prediction:", prediction["label"])
            else:
                st.write("Error:", response.status_code, response.text)

        except Exception as e:
            st.write("An error occurred:", str(e))



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
