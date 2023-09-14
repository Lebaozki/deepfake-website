import streamlit as st

col1, col2 = st.columns([0.5,3])
with col1:
    st.image("images/DeepFakeDetection_Logo.png", width=80)
with col2:
    st.title('Meet Our Team')

st.header("The Minds Behind Fake Face Detection App")

st.write(
    "Our team comprises a diverse group of passionate experts in computer vision, machine learning and data science. With a shared commitment to making the internet a safer place, we bring a wealth of experience and expertise to the table."
)

st.write("Meet the Faces Behind Fake Face Detection:")

a = "[Vincent Rachor](https://www.linkedin.com/in/vincent-rachor/): Vincent holds both a bachelor's and master's degree in mechatronics and digital technologies from the Technical University of Munich. He is highly passionate about web development, data science, machine learning, and natural language processing."
b = "[Yuan Tian Li](https://www.linkedin.com/in/yuantian06/): Yuan is a strategy consultant based in Zurich. With a background in Business Analytics, she explored Python and data engineering through a bootcamp, opening exciting opportunities in the digital and data-driven realm. Yuantian's commitment to continuous learning drives her journey in the world of digital technologies."
c = "[Malvina Guex](https://www.linkedin.com/in/malvinaguex/): Malvina started in material engineering but swiftly transitioned to fintech as a data analyst in Zurich. Her deep fascination with data led her to embrace entrepreneurship and deepen her expertise in data science. Malvina's mission involves seeking like-minded co-founders for impactful ventures."
d = "[Sergio Estebanez Alvarez](https://www.linkedin.com/in/sergio-estebanez-alvarez/): Sergio, with a Bachelor's in Systems Engineering, excels in the audiovisual industry as a film editor, director, and producer. His creative talents extend to creating TV news content. Sergio's growing interest in data science, especially in AI and machine learning, merges his rich audiovisual experience with the dynamic world of data science."
lst = [a, b, c, d]
s = ''

for i in lst:
    s += "- " + i + "\n"

st.markdown(s)
