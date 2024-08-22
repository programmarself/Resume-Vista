import streamlit as st
import os
from dotenv import load_dotenv
import pandas as pd
from io import BytesIO

# Load environment variables from .env file
load_dotenv()

# Access the API key (for demonstration purposes)
API_KEY = os.getenv("API_KEY")

def generate_resume(data):
    # Create a DataFrame for the resume content
    resume_df = pd.DataFrame(data)

    # Convert DataFrame to Excel
    buffer = BytesIO()
    with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
        resume_df.to_excel(writer, index=False, sheet_name='Resume')
        writer.save()
    buffer.seek(0)
    return buffer

def main():
    st.title("Interactive Digital Resume")

    st.header("Enter Your Information")

    with st.form("resume_form"):
        name = st.text_input("Full Name")
        profession = st.text_input("Profession")
        key_skills = st.text_area("Key Skills")
        experiences = st.text_area("Experience (Format: Job Title - Company - Date Range - Achievements)")
        education = st.text_area("Education (Format: Degree - Institution - Date Range)")
        skills = st.text_area("Skills (Format: Skill1, Skill2, Skill3)")
        projects = st.text_area("Projects (Format: Project Title - Description - Technologies Used)")
        contact_email = st.text_input("Email")
        linkedin_profile = st.text_input("LinkedIn Profile")

        submit_button = st.form_submit_button("Generate Resume")

    if submit_button:
        # Prepare data for the resume
        resume_data = {
            "Name": [name],
            "Profession": [profession],
            "Key Skills": [key_skills],
            "Experience": [experiences],
            "Education": [education],
            "Skills": [skills],
            "Projects": [projects],
            "Contact Email": [contact_email],
            "LinkedIn Profile": [linkedin_profile]
        }

        # Generate resume file
        resume_file = generate_resume(resume_data)
        
        st.success("Resume generated successfully!")

        st.download_button(
            label="Download Resume",
            data=resume_file,
            file_name="resume.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

if __name__ == "__main__":
    main()
