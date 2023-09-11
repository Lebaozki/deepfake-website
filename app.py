import streamlit as st
from PIL import Image
import requests
from dotenv import load_dotenv
import os
# Set page title and favicon
st.set_page_config(
    page_title="Deepfake Detection",
    page_icon=":smiley:",
)

# with open ('style.css') as f:
#     st.markdown(f'<style>{f.read}</style>', unsafe_allow_html=True)

# Define Streamlit app content
st.title("Deepfake Detection")

# Subheading
st.subheader("Is your image real?")

url = 'https://deepfakepreproc-abexurulqa-ew.a.run.app/docs'

# File upload widget
img_file_buffer = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if img_file_buffer is not None:

  col1, col2 = st.columns(2)

  with col1:
    ### Display the image user uploaded
    st.image(Image.open(img_file_buffer), caption="Here's the image you uploaded ☝️")

  with col2:
    with st.spinner("Wait for it..."):
      ### Get bytes from the file buffer
      img_bytes = img_file_buffer.getvalue()

      ### Make request to  API (stream=True to stream response as bytes)
      res = requests.post(url + "/upload_image", files={'img': img_bytes})

      if res.status_code == 200:
        ### Display the image returned by the API
        st.image(res.content, caption="Image returned from API ☝️")
      else:
        st.markdown("**Oops**, something went wrong 😓 Please try again.")
        print(res.status_code, res.content)

# Add any additional content or styling as needed
#Test commit
