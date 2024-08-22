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
    }
    .section-title {
        color: #4682B4;
        font-size: 24px;
        font-weight: bold;
    }
    .section {
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown(f"<div class='title'>{
