import streamlit as st

# Load the secret API key from Streamlit's secrets management
api_key = st.secrets["api_key"]

# Title of the app
st.title("Resume Vista")

# Personal Information
st.header("Personal Information")
st.write("**Name:** John Doe")
st.write("**Email:** john.doe@example.com")
st.write("**Phone:** (123) 456-7890")
st.write("**LinkedIn:** [linkedin.com/in/johndoe](https://linkedin.com/in/johndoe)")
st.write("**GitHub:** [github.com/johndoe](https://github.com/johndoe)")

# About Me Section
st.header("About Me")
st.write("""
I am a passionate software developer with experience in building web applications and 
working with various technologies. I enjoy problem-solving and learning new things. 
I thrive in collaborative environments and am always eager to contribute to team success.
""")

# Experience Section
st.header("Experience")
st.subheader("Software Developer at Tech Company")
st.write("""
**Duration:** January 2020 - Present  
**Responsibilities:**
- Developed and maintained web applications using Python and JavaScript.
- Collaborated with cross-functional teams to design and implement new features.
- Optimized performance and scalability of applications.
""")

st.subheader("Junior Developer at Another Tech Company")
st.write("""
**Duration:** June 2018 - December 2019  
**Responsibilities:**
- Assisted in the development of web applications and debugging issues.
- Participated in code reviews and contributed to documentation.
""")

# Education Section
st.header("Education")
st.subheader("Bachelor of Science in Computer Science")
st.write("""
**University Name**  
**Graduation Year:** 2018  
**Relevant Coursework:** Data Structures, Algorithms, Web Development, Databases
""")

# Skills Section
st.header("Skills")
st.write("""
- **Programming Languages:** Python, JavaScript, HTML, CSS
- **Frameworks and Libraries:** Django, Flask, React, Node.js
- **Tools:** Git, Docker, AWS
- **Soft Skills:** Problem-solving, Communication, Teamwork
""")

# Projects Section
st.header("Projects")
st.subheader("Project One")
st.write("""
A brief description of what the project is about, the technologies used, and your role in it.
""")

st.subheader("Project Two")
st.write("""
A brief description of what the project is about, the technologies used, and your role in it.
""")

# Footer
st.header("Contact Me")
st.write("Feel free to reach out via email or LinkedIn!")

# Example usage of the API key (for demonstration purposes)
st.write(f"API Key (for development purposes): {api_key}")
