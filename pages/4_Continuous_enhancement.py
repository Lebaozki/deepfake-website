import streamlit as st

col1, col2 = st.columns([0.5,3])
with col1:
    st.image("images/DeepFakeDetection_Logo.png", width=80)
with col2:
    st.title('Continuous Enhancement')

st.header("Your Feedback Shapes Our Future")
st.write(
    "At Fake Face Detection, we are committed to continuous improvement. We understand that online threats are constantly evolving, and we're dedicated to staying one step ahead. Your feedback is invaluable in helping us refine our app and services."
)

st.header("Ways You Can Help Us Improve")
st.write(
    "Share your experiences and suggestions in our community forums."
)
st.write(
    "Report any false positives or negatives to help us fine-tune our algorithms."
)
st.write(
    "Stay informed about emerging online deception techniques and share your insights."
)
st.write(
    "Join us in our mission to create a safer online world for everyone."
)
st.write(
    "By offering these sections on your website, you'll provide visitors with comprehensive information about your Fake Face Detection App, your mission, the team behind it, and the collaborative effort to improve online security."
)

st.write(
    "Join us in our mission to create a safer online world for everyone."
)

st.write("These are the links to")

a = 'the repository: [DeepFakeDetection GitHub Repository](https://github.com/RayVinc/DeepFakeDetection)'
b = 'the web site repository: [Deepfake Detection Website GitHub Repository](https://github.com/Lebaozki/deepfake-website)'
c = 'this website: [Deepfake Detection Web App](https://fakefacedetection.streamlit.app/)'
lst = [a, b, c]
s = ''
for i in lst:
    s += "- " + i + "\n"
st.markdown(s)
