import streamlit as st
from PIL import Image
import os  # For environment variable access

# Define resume data
resume_data = {
    "name": "Your Name",
    "title": "Your Title (e.g., Software Engineer)",
    "email": "your_email@example.com",
    "phone": "Your Phone Number",
    "linkedin": "https://www.linkedin.com/in/your_linkedin_profile",
    "github": "https://github.com/your_github_username",
    "skills": ["Python", "Machine Learning", "Data Science", "Deep Learning"],
    "projects": [
        {
            "title": "Project 1",
            "description": "Brief description of Project 1",
            "link": "https://github.com/your_repo/project1"
        },
        # Add more projects as needed
    ],
    "experience": [
        {
            "company": "Company Name",
            "position": "Your Position",
            "start_date": "Month Year",
            "end_date": "Month Year (or Present)",
            "description": "Your experience at the company"
        },
        # Add more experience as needed
    ],
    "education": [
        {
            "degree": "Your Degree",
            "field": "Your Field of Study",
            "university": "University Name",
            "graduation_date": "Month Year"
        },
        # Add more education as needed
    ]
}

def create_resume():
    st.title("Your Name")
    st.subheader(resume_data["title"])

    col1, col2 = st.columns(2)
    with col1:
        st.write("**Contact Information:**")
        st.write(f"Email: {resume_data['email']}")
        st.write(f"Phone: {resume_data['phone']}")
        st.write(f"LinkedIn: {resume_data['linkedin']}")
        st.write(f"GitHub: {resume_data['github']}")

    with col2:
        st.write("**Skills:**")
        for skill in resume_data["skills"]:
            st.write(f"- {skill}")

    st.write("**Projects:**")
    for project in resume_data["projects"]:
        st.write(f"**{project['title']}**")
        st.write(project["description"])
        st.write(f"[Link]({project['link']})")

    st.write("**Experience:**")
    for exp in resume_data["experience"]:
        st.write(f"**{exp['company']}** - **{exp['position']}**")
        st.write(f"{exp['start_date']} - {exp['end_date']}")
        st.write(exp["description"])

    st.write("**Education:**")
    for edu in resume_data["education"]:
        st.write(f"**{edu['degree']}** in **{edu['field']}** from **{edu['university']}**")
        st.write(f"Graduated: {edu['graduation_date']}")

# Access API key using environment variable or Streamlit secrets (choose one)
# Option 1: Using environment variable (recommended)
# api_key = os.environ.get("MY_API_KEY")

# Option 2: Using Streamlit secrets (alternative)
 api_key = st.secrets["my_api_key"]  # Uncomment if using Streamlit secrets

# Use the API key in your Streamlit app (if needed)
# ... (Your code using the API key)

if __name__ == "__main__":
    create_resume()