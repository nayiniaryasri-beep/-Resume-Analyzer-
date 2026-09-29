import streamlit as st

# Page settings
st.set_page_config(
    page_title="Resume Analyzer",
    page_icon="📄",
    layout="centered"
)

# ---------------- INTERNAL CSS ----------------
st.markdown("""
<style>

    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #dbeafe, #f0fdf4);
    }

    /* Main title */
    h1 {
        text-align: center;
        color: #1e3a8a;
        font-size: 42px;
        font-weight: bold;
    }

    /* Header */
    h2 {
        color: #1e40af;
    }

    /* Subheaders */
    h3 {
        color: #2563eb;
    }

    /* Normal text */
    p {
        color: #374151;
        font-size: 16px;
    }

    /* Text input */
    .stTextInput input {
        border: 2px solid #93c5fd;
        border-radius: 10px;
        padding: 10px;
        font-size: 16px;
    }

    .stTextInput input:focus {
        border-color: #2563eb;
        box-shadow: 0 0 5px #93c5fd;
    }

    /* Select boxes */
    .stSelectbox div {
        border-radius: 10px;
    }

    /* Slider */
    .stSlider {
        padding: 10px;
    }

    /* File uploader */
    [data-testid="stFileUploader"] {
        background-color: white;
        border: 2px dashed #60a5fa;
        border-radius: 12px;
        padding: 15px;
    }

    /* Button */
    .stButton button {
        width: 100%;
        background-color: #2563eb;
        color: white;
        border: none;
        border-radius: 10px;
        padding: 12px;
        font-size: 18px;
        font-weight: bold;
    }

    /* Button hover */
    .stButton button:hover {
        background-color: #1d4ed8;
        color: white;
    }

    /* Divider */
    hr {
        border: 1px solid #bfdbfe;
    }

    /* Success / Warning / Info boxes */
    .stAlert {
        border-radius: 10px;
    }

</style>
""", unsafe_allow_html=True)


# ---------------- APPLICATION ----------------

# Title
page_title="Resume Builder",
st.header("Welcome to the Resume Web Application")

st.write("Create and manage your resume details easily.")

st.markdown(
    "**This application helps users enter their personal, educational, "
    "and resume information.**"
)

st.divider()


# Personal Information
st.subheader("👤 Personal Information")

name = st.text_input("Enter your full name")

email = st.text_input("Enter your email address")

phone = st.text_input("Enter your phone number")

gender = st.radio(
    "Select your gender",
    ("Male", "Female", "Other")
)

st.divider()


# Education Details
st.subheader("🎓 Education Details")

graduation = st.date_input(
    "Enter your graduation date"
)
cgpa = st.number_input(
    "Enter your CGPA",
    min_value=0.0,
    max_value=10.0,
    value=7.0,
    step=0.1
)
st.write("Your CGPA:", cgpa)

st.divider()


# Skills
st.subheader("💻 Skills")

skills = st.multiselect(
    "Select your skills",
    [
        "Python",
        "Java",
        "C",
        "HTML",
        "CSS",
        "JavaScript",
        "SQL",
        "Machine Learning",
        "Artificial Intelligence"
    ]
)

st.divider()


# Resume Upload
st.subheader("📁 Resume Upload")

file = st.file_uploader(
    "Upload your resume",
    type=["pdf", "docx"]
)


# Additional Information
st.subheader("🎨 Additional Information")

color = st.color_picker(
    "Choose your favorite color",
    "#D1C8C7"
)

agreement = st.checkbox(
    "I agree to the terms and conditions"
)


# Submit button
if st.button("🚀 Analyze Resume"):

    if name == "":
        st.warning("Please enter your name.")

    elif email == "":
        st.warning("Please enter your email address.")

    elif phone == "":
        st.warning("Please enter your phone number.")

    elif file is None:
        st.warning("Please upload your resume.")

    elif not agreement:
        st.warning("Please accept the terms and conditions.")

    else:
        st.success("✅ Resume submitted successfully!")

        st.write("### 📋 Resume Details")

        st.write("**Name:**", name)
        st.write("**Email:**", email)
        st.write("**Phone:**", phone)
        st.write("**Gender:**", gender)
        st.write("**Graduation Date:**", graduation)
        st.write("**CGPA:**", cgpa)
        st.write("**Skills:**", ", ".join(skills))

        st.info("🎉 Your resume has been successfully analyzed!")