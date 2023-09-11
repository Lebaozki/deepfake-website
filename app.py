import streamlit as st
import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import ast

# Set page title and favicon
st.set_page_config(
    page_title="Deepfake Detection",
    page_icon=":smiley:",
)

# Define Streamlit app content
st.title("Deepfake Detection")

# Subheading
st.subheader("Is your image real?")

url = 'https://deepfakepreproc-abexurulqa-ew.a.run.app'

# File upload widget
img_file_buffer = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Check if an image is uploaded

if img_file_buffer is not None:

  col1, col2 = st.columns(2)

  with col1:
    ### Display the image user uploaded
    st.image(Image.open(img_file_buffer), caption="Uploaded Image")


  with col2:
    with st.spinner("Wait for it..."):
        ### Get bytes from the file buffer
        img_bytes = img_file_buffer.getvalue()

        ### Make request to  API (stream=True to stream response as bytes)
        res = requests.post(url + "/upload_image", files={'img': img_bytes})

        if res.status_code == 200:
            #change code if backend gives dict (remove .tobytes())
            answer_dict = ast.literal_eval(res.content.decode('utf-8'))

            if answer_dict["prob"] == 'real':
                response_printout = "✅ " + answer_dict["prob"].upper() + " ✅"
            elif answer_dict["prob"] == 'fake':
                response_printout = "❌ " + answer_dict["prob"].upper() + " ❌"
            else:
                response_printout = "❓ ...unreadable... ❓"

            with st.container():
                st.markdown("<br>", unsafe_allow_html=True)
                st.markdown("<br>", unsafe_allow_html=True)
                st.markdown("<br>", unsafe_allow_html=True)
                st.markdown('<div style="text-align: center; font-size: 25px;">This image seems to be:</div>', unsafe_allow_html=True)
                st.markdown(f'<div style="text-align: center; font-size: 50px;"><b>{response_printout}</b></div>', unsafe_allow_html=True)
                #st.write(answer_dict['prob'])

        else:
            st.markdown("**Oops**, something went wrong. Please try again.")
            st.write(res.status_code, res.content)
            print((res.status_code, res.content))


# Add any additional content or styling as needed
#Test commit
st.markdown("## Disclaimer")
st.write(
    "This project is an academic endeavor. While the results of our predictive model are impressive, we are not the definitive tool to prove anything. Please use it with caution and discretion."
)

st.markdown("""
  <style>
    css-1v0mbdj.etr89bj1 > img{
      border-radius: 50%;
    }
  </style>
""", unsafe_allow_html=True)

# Add any additional content or styling as needed
#Test commit
