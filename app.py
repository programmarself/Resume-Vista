import streamlit as st

# Access secret key from Streamlit secrets
SECRET_KEY = st.secrets.get("SECRET_KEY", "default-secret-key")

# Sample resume data with detailed information
resume_data = {
    "Name": "Irfan Ullah Khan",
    "Date of Birth": "01/08/1992",
    "Nationality": "Pakistani",
    "Gender": "Male",
    "Phone Number": "(+92) 03021906646 (Mobile)",
    "Email": "programmarself@gmail.com",
    "Website": "https://flowcv.me/ikm",
    "LinkedIn": "www.linkedin.com/in/irfan-ullah-khan-4a2871208",
    "WhatsApp Messenger": "+9203021906646",
    "Address": "District and Post Office Lakki Marwat, Village Achu Khel, 28420, LAKKI MARWAT, Pakistan",
    "Current Focus": "Work on and busy with Machine Learning, Data Science, AI & GCP",
    "Education": [
        {
            "Degree": "BS (Computer Science)",
            "Institution": "Virtual University of Pakistan",
            "Duration": "01/01/2019 – 01/08/2024",
            "Website": "https://www.vu.edu.pk/",
            "Location": "Peshawar, Pakistan"
        },
        {
            "Degree": "ICS (Intermediate in Computer Science)",
            "Institution": "Govt Degree College Wana",
            "Location": "Lakki Marwat, Pakistan"
        },
        {
            "Degree": "SSC (Secondary School Certificate)",
            "Institution": "GHS (Govt High School No 2)",
            "Completion Date": "26/01/2015",
            "Location": "Peshawar, Pakistan"
        },
        {
            "Degree": "DIT (Diploma in Information Technology)",
            "Institution": "GTVC (Govt Technical & Vocational College)",
            "Website": "https://www.kpttb.gov.pk/",
            "Location": "Peshawar, Pakistan"
        }
    ],
    "Languages": {
        "Mother Tongue": "Pashto",
        "English": {"Listening": "C1", "Reading": "C1", "Spoken Production": "C1", "Spoken Interaction": "C1", "Writing": "C1"},
        "Urdu": {"Listening": "C2", "Reading": "C2", "Spoken Production": "C2", "Spoken Interaction": "C2", "Writing": "C2"},
        "Arabic": {"Listening": "A1", "Reading": "A1", "Spoken Production": "A1", "Spoken Interaction": "A1", "Writing": "A1"}
    },
    "Skills": ["Microsoft Office", "Machine Learning", "AI", "Data Science", "GCP"],
    "Projects": [
        {
            "Title": "Diabetes Prediction using Classification Method",
            "Domain/Category": "Machine Learning, Data Science",
            "Description": (
                "This model helps patients and doctors diagnose diabetes. "
                "It predicts based on a dataset using various machine learning algorithms. "
                "Includes data pre-processing, training with Neural Networks, and evaluation using metrics such as accuracy, precision, recall, and F1 score."
            ),
            "Skills": ["Machine Learning", "Data Science"],
            "Programming Language": "Python",
            "Framework": "Anaconda"
        }
    ],
    "Certifications": {
        "Machine Learning": [
            "Machine Learning (Stanford University & DeepLearning.AI)",
            "Mathematics for Machine Learning (Imperial College London)",
            "IBM Machine Learning Specialization"
        ],
        "Data Science": [
            "Introduction to Data Science Specialization (IBM)",
            "Data Science Specialization (IBM)",
            "Applied Data Science Specialization (IBM)",
            "Data Science Fundamentals with Python and SQL Specialization (IBM)",
            "Google Data Analytics Specialization"
        ],
        "AI": [
            "Applied AI Specialization (IBM)",
            "AI Foundations for Everyone Specialization (IBM)",
            "AI for Good Specialization (DeepLearning.AI)",
            "AI Engineering Specialization (IBM)"
        ],
        "Programming Languages": [
            "Python for Everybody Specialization (University of Michigan)",
            "Google IT Automation with Python",
            "Python | C++ | Cyber Security | Network Essentials (Cisco)"
        ]
    },
    "Hobbies and Interests": ["Reading", "Writing", "Computing", "Cricket", "Volleyball"]
}

# Streamlit app layout
st.markdown("""
    <style>
    .title {
        color: #1E90FF;
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    .subheader {
        color: #4682B4;
        font-size: 24px;
        font-weight: bold;
        margin-top: 20px;
    }
    .section {
        margin-bottom: 20px;
    }
    .card {
        background-color: #f5f5f5;
        padding: 15px;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown(f"<div class='title'>{resume_data['Name']}'s Resume</div>", unsafe_allow_html=True)

# Personal Information
st.markdown("<div class='card'><h2 class='subheader'>Personal Information</h2></div>", unsafe_allow_html=True)
st.write(f"**Date of Birth:** {resume_data['Date of Birth']}")
st.write(f"**Nationality:** {resume_data['Nationality']}")
st.write(f"**Gender:** {resume_data['Gender']}")
st.write(f"**Phone Number:** {resume_data['Phone Number']}")
st.write(f"**Email:** [Email]({resume_data['Email']})")
st.write(f"**Website:** [Website]({resume_data['Website']})")
st.write(f"**LinkedIn:** [LinkedIn Profile]({resume_data['LinkedIn']})")
st.write(f"**WhatsApp Messenger:** {resume_data['WhatsApp Messenger']}")
st.write(f"**Address:** {resume_data['Address']}")
st.write(f"**Current Focus:** {resume_data['Current Focus']}")

# Education
st.markdown("<div class='card'><h2 class='subheader'>Education</h2></div>", unsafe_allow_html=True)
for education in resume_data['Education']:
    st.write(f"**{education['Degree']}**")
    st.write(f"**Institution:** {education['Institution']}")
    st.write(f"**Duration:** {education.get('Duration', 'N/A')}")
    if 'Website' in education:
        st.write(f"**Website:** [Institution Website]({education['Website']})")
    st.write(f"**Location:** {education['Location']}")
    st.write("---")

# Language Skills
st.markdown("<div class='card'><h2 class='subheader'>Language Skills</h2></div>", unsafe_allow_html=True)
for language, skills in resume_data['Languages'].items():
    if language == "Mother Tongue":
        st.write(f"**{language}:** {skills}")
    else:
        st.write(f"**{language}:**")
        for skill, level in skills.items():
            st.write(f"- **{skill}:** {level}")

# Skills
st.markdown("<div class='card'><h2 class='subheader'>Skills</h2></div>", unsafe_allow_html=True)
st.write(", ".join(resume_data['Skills']))

# Projects
st.markdown("<div class='card'><h2 class='subheader'>Projects</h2></div>", unsafe_allow_html=True)
for project in resume_data['Projects']:
    st.write(f"**{project['Title']}**")
    st.write(f"**Domain/Category:** {project['Domain/Category']}")
    st.write(f"**Description:** {project['Description']}")
    st.write(f"**Skills:** {', '.join(project['Skills'])}")
    st.write(f"**Programming Language:** {project['Programming Language']}")
    st.write(f"**Framework:** {project['Framework']}")
    st.write("---")

# Certifications
st.markdown("<div class='card'><h2 class='subheader'>Certifications</h2></div>", unsafe_allow_html=True)
for category, certs in resume_data['Certifications'].items():
    st.write(f"**{category}:**")
    for cert in certs:
        st.write(f"- {cert}")
    st.write("---")

# Hobbies and Interests
st.markdown("<div class='card'><h2 class='subheader'>Hobbies and Interests</h2></div>", unsafe_allow_html=True)
st.write(", ".join(resume_data['Hobbies and Interests']))

# Add a button to download the resume (optional)
if st.button('Download Resume'):
    st.write("Resume downloaded!")
