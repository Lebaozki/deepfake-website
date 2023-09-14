import streamlit as st

col1, col2 = st.columns([0.5,3])
with col1:
    st.image("images/DeepFakeDetection_Logo.png", width=80)
with col2:
    st.title('Fake Face Detection App')

st.header("Enhancing Online Security and Trust")

st.write(
    "Welcome to the Fake Face Detection App, your trusted partner in ensuring online authenticity and detecting AI generated fake face images. We aim to distinguish between real images and AI-generated images, contributing to the fight against disinformation and fraud, but also for fun. Here's why it matters:"
)

st.write(
    "AI technology has the potential to create highly convincing fake images, which can be used for malicious purposes. By developing effective AI-generated image detection methods, we can help protect individuals and organizations from falling victim to misinformation and scams. Our project focuses on detecting these AI-generated GAN alterations and enhancing media trustworthiness. 🕵️‍♂️"
    )

st.write("Key Features:")

a = 'User-friendly Interface: Easily upload images or URLs for analysis with a simple and intuitive user interface.'
b = 'Comprehensive Reporting: Receive detailed reports on the authenticity of detected images, helping you make informed decisions.'
c = 'Educational Resources: Access educational materials to understand the techniques used in fake face creation.'
d = "Continuous Improvement: We're committed to constant refinement to stay ahead of emerging threats."
lst = [a, b, c, d]
s = ''

for i in lst:
    s += "- " + i + "\n"

st.markdown(s)
