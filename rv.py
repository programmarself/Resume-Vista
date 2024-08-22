import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the API key
API_KEY = os.getenv("API_KEY")

# Define your resume data
def main():
    st.title("Your Name - Digital Resume")

    st.header("About Me")
    st.write("""
    Hi! I'm [Your Name], a [Your Profession] with expertise in [Your Key Skills].
    I have experience working on [Your Key Projects or Areas of Expertise].
    """)

    st.header("Experience")
    st.write("**Job Title at Company Name**")
    st.write("*Date Range*")
    st.write("""
    - Key responsibility or achievement
    - Another responsibility or achievement
    """)

    st.write("**Another Job Title at Another Company**")
    st.write("*Date Range*")
    st.write("""
    - Key responsibility or achievement
    - Another responsibility or achievement
    """)

    st.header("Education")
    st.write("**Degree Name**")
    st.write("Institution Name")
    st.write("*Date Range*")

    st.header("Skills")
    st.write("""
    - Skill 1
    - Skill 2
    - Skill 3
    """)

    st.header("Projects")
    st.write("**Project Title**")
    st.write("""
    Description of the project and your role.
    - Technologies used: Tech1, Tech2
    """)

    st.header("Contact")
    st.write("Email: [your.email@example.com](mailto:your.email@example.com)")
    st.write("LinkedIn: [Your LinkedIn Profile](https://www.linkedin.com/in/yourprofile)")

    # Example usage of API_KEY (for demonstration purposes)
    st.write(f"API Key: {API_KEY}")

if __name__ == "__main__":
    main()
