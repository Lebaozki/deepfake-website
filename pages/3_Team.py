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

a = "[Vincent Rachor](https://www.linkedin.com/in/vincent-rachor/): Vincent holds a bachelor's degree in mechatronics and a master's degree in digital technologies from the Technical University of Munich. His professional journey began as a developer at Infineon, where he made significant contributions to projects involving embedded systems, sensors, and microcontrollers. His expertise extends to web development, data science, machine learning, and natural language processing. Vincent's passion lies in creating and sharing innovative solutions across diverse domains on GitHub."
b = "[Yuan Tian Li](https://www.linkedin.com/in/yuantian06/): Yuan is a strategy consultant currently based in Zurich. With a background in Business Analytics, she pursued further knowledge and skills through a bootcamp to delve into Python and data engineering. This endeavor opens up exciting possibilities for him in the digital and data-driven realm as he explores various career avenues. Yuantian's commitment to continuous learning and adaptation drives his journey in the world of digital technologies."
c = "[Malvina Guex](https://www.linkedin.com/in/malvinaguex/): Malvina's academic background lies in material engineering, but her career has taken intriguing turns. Starting as a data analyst in a fintech company in Zurich, she swiftly transitioned into a role as a product owner/manager. Her profound fascination with data prompted her to embark on a path of continuous learning, particularly in data science. In March 2023, she took a leap of faith, leaving her job to embrace entrepreneurship and deepen her expertise in data science. Malvina's current mission includes searching for like-minded co-founders to embark on a journey of positive impact on the world."
d = "[Sergio Estebanez Alvarez](https://www.linkedin.com/in/sergio-estebanez-alvarez/): Meet Sergio Estebanez Alvarez, an experienced professional with a unique blend of skills. Armed with a Bachelor's degree in Systems Engineering, Sergio has predominantly carved his path in the audiovisual industry as a film editor. His creative flair has led him to direct, edit, and produce captivating short and feature films, weaving engaging stories and evoking emotions. Over the last four years, Sergio has also been instrumental in creating TV news content, covering significant events in special venues. In addition to his audiovisual expertise, Sergio's curiosity for data science, particularly in the realms of AI and machine learning, has grown significantly. By merging his extensive experience in the audiovisual industry with his newfound interest in data science, Sergio is poised to explore the intriguing intersection of these two dynamic worlds."
lst = [a, b, c, d]
s = ''

for i in lst:
    s += "- " + i + "\n"

st.markdown(s)
