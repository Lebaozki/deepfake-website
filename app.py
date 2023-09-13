import streamlit as st
import pandas as pd
import requests
from PIL import Image
from io import BytesIO
import ast
import plotly.express as px

url = 'https://deepfake-abexurulqa-ew.a.run.app'
res = ""

# Set page title and favicon
st.set_page_config(
    page_title="Deepfake Detection",
    page_icon=Image.open("images/DeepFakeDetection_FavIcon.png"),
    layout="wide",
    initial_sidebar_state='collapsed'
)
#st.sidebar.title("Menu")
#st.sidebar.image("DeepFakeDetection_Logo.png", use_column_width=True, width=150)

col1, col2, col3 = st.columns([1,2,1])

with col1:
    st.image("images/DeepFakeDetection_Logo.png", width=200, caption="", use_column_width=False)


with col2:
    st.title("Deepfake Detection")
    # Logo and header styling with HTML/CSS
    header_style = """
        <style>
            .stApp {
                text-align: center;
            }
            .header-text {
                font-size: 24px;
                font-weight: bold;
            }
        </style>
    """

    st.markdown(header_style, unsafe_allow_html=True)
    st.markdown("<div class='header-text'>Is your image real?</div>", unsafe_allow_html=True)

    # File upload widget
    img_file_buffer = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])


if img_file_buffer is not None:
    col1, col2, col3, col4 = st.columns([1,2,2,1])
    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        #st.write('Uploaded Image')
        ### Display the image user uploaded
        st.image(Image.open(img_file_buffer), caption="Uploaded Image", width=300)
        with st.spinner("Wait for it..."):
            ### Get bytes from the file buffer
            img_bytes = img_file_buffer.getvalue()

            ### Make request to  API (stream=True to stream response as bytes)
            res = requests.post(url + "/upload_image", files={'img': img_bytes})
        with col3:
            #st.markdown("<br><br>", unsafe_allow_html=True)
            if res.status_code == 200:
                #change code if backend gives dict (remove .tobytes())
                answer_dict = ast.literal_eval(res.content.decode('utf-8'))
                answer = answer_dict['prob']
                if answer[0] > answer[1]:
                    res = "FAKE"
                    perc = answer[0]
                else:
                    res = "REAL"
                    perc = answer[1]
                data_dict = {'Fake': answer[0], 'Real': answer[1]}
                if answer[1]:
                    df = pd.DataFrame(list(data_dict.items()), columns=['Category', 'Percentage'])
                    custom_colors = {'Fake': '#D42B42', 'Real': '#42D42B'}
                    fig = px.bar(df,
                                 x='Category',
                                 y='Percentage',
                                 range_y=[0,1],
                                 color='Category',
                                 color_discrete_sequence=[custom_colors[cat] for cat in df['Category']],
                                 opacity=0.8)
                    st.plotly_chart(fig)
                else:
                    response_printout = f"❓ ...unreadable... ({answer}) ❓"

                # with st.container():
                #     st.markdown("<br>", unsafe_allow_html=True)
                #     st.markdown("<br>", unsafe_allow_html=True)
                #     st.markdown("<br>", unsafe_allow_html=True)
                    #st.markdown('<div style="text-align: center; font-size: 25px;">This image seems to be:</div>', unsafe_allow_html=True)
                    #st.markdown(f'<div style="text-align: center; font-size: 50px;"><b>{response_printout}</b></div>', unsafe_allow_html=True)
                    #st.write(answer_dict['prob'])

            else:
                st.markdown("**Oops**, something went wrong. Please try again.")
                st.write(res.status_code, res.content)
                print((res.status_code, res.content))
else:
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        screenshot = Image.open('images/SlideSwirl.png')
        st.image(screenshot, use_column_width = "always")

with col3:
    pass

if res == "":
    pass
else:
    st.write(f'<span style="font-size: 20px; font-weight: bold;">I am {round(perc*100, 2)}% certain this image is {res}</span>', unsafe_allow_html=True)


st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("## Disclaimer")
st.write(
    "This deepfake detection tool is provided for informational purposes only. While we strive for accuracy, it may produce false positives and false negatives. Use this tool cautiously and consider it as an aid, not a definitive judgment. It is not a substitute for professional analysis or legal advice. We do not guarantee its accuracy or reliability. By using this tool, you agree to these terms and conditions."
)
