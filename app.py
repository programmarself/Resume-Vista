import streamlit as st

# Access secret key from Streamlit secrets
SECRET_KEY = st.secrets.get("SECRET_KEY", "default-secret-key")

# Sample resume data
resume_data = {
    "Name": "John Doe",
    "Email": "john.doe@example.com",
    "Phone": "+1234567890",
    "LinkedIn": "linkedin.com/in/johndoe",
    "Summary": "Experienced software developer with a passion for building scalable applications.",
    "Skills": ["Python", "Streamlit", "Data Analysis", "Machine Learning"],
    "Experience": [
        {
            "Company": "Tech Inc.",
            "Position": "Software Engineer",
            "Duration": "Jan 2020 - Present",
            "Responsibilities": [
                "Developed web applications using Streamlit.",
                "Collaborated with cross-functional teams.",
                "Optimized data processing pipelines."
            ]
        },
        {
            "Company": "Web Solutions",
            "Position": "Junior Developer",
            "Duration": "Jun 2018 - Dec 2019",
            "Responsibilities": [
                "Worked on frontend development.",
                "Assisted in backend API integrations.",
                "Performed unit testing and debugging."
            ]
        }
    ]
}

# Streamlit app layout
st.title(f"{resume_data['Name']}'s Resume")
st.subheader("Contact Information")
st.write(f"**Email:** {resume_data['Email']}")
st.write(f"**Phone:** {resume_data['Phone']}")
st.write(f"**LinkedIn:** [LinkedIn Profile]({resume_data['LinkedIn']})")

st.subheader("Summary")
st.write(resume_data['Summary'])

st.subheader("Skills")
st.write(", ".join(resume_data['Skills']))

st.subheader("Experience")
for job in resume_data['Experience']:
    st.write(f"**{job['Company']}**")
    st.write(f"**Position:** {job['Position']}")
    st.write(f"**Duration:** {job['Duration']}")
    st.write("**Responsibilities:**")
    for responsibility in job['Responsibilities']:
        st.write(f"- {responsibility}")


