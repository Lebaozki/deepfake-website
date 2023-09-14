import streamlit as st

col1, col2 = st.columns([0.5,3])
with col1:
    st.image("images/DeepFakeDetection_Logo.png", width=80)
with col2:
    st.title('Our Mission and Vision')

st.header("Building a Safer Online World")

st.write(
    "At Fake Face Detection, our mission is clear: to create a safer and more trustworthy online environment. We're dedicated to combating the proliferation of fake profiles, deepfakes, and manipulated images across the web. By harnessing the power of artificial intelligence and machine learning, we aim to empower individuals, businesses, and internet communities to protect themselves against online deception."
)

st.header("Our Vision")

st.write(
    "To empower individuals with the knowledge and tools to distinguish between real and AI-generated images, fostering a more informed and discerning online community. We strive to provide accessible educational resources that promote digital literacy, media trustworthiness, and online security."
    )
st.write(
    "This vision statement aligns with the educational aspect of your project, emphasizing the goal of educating individuals rather than becoming a corporate leader in a specific field."
    )
