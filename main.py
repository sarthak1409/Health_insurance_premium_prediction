# codebasics ML course: codebasics.io, all rights reserved

import streamlit as st
from predcition_helper1 import predict

# Page configuration
st.set_page_config(page_title="Health Insurance Predictor", layout="wide")

# Custom CSS styling
st.markdown("""
    <style>
        .main {
            background-color: #f9f9f9;
        }
        h1 {
            color: #0A2647;
        }
        .stButton>button {
            background-color: #144272;
            color: white;
            border-radius: 10px;
            height: 3em;
            width: 100%;
            font-size: 18px;
        }
        .stSelectbox label, .stNumberInput label {
            font-size: 16px;
            font-weight: 600;
        }
        .block-container {
            padding: 2rem 3rem;
        }
    </style>
""", unsafe_allow_html=True)

# App title and intro
st.title("🏥 Health Insurance Cost Predictor")
st.caption("Get a quick estimate of your health insurance premium using key personal and lifestyle factors.")

# Input form
with st.form("insurance_form"):
    st.subheader("🔢 Basic Information")
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input('Age', min_value=18, max_value=100, step=1, help="Enter your age (18–100)")
    with col2:
        number_of_dependants = st.number_input('Number of Dependants', min_value=0, max_value=20, step=1)
    with col3:
        income_lakhs = st.number_input('Income in Lakhs (INR)', min_value=0, max_value=200, step=1)

    st.subheader("💼 Lifestyle & Coverage")
    col4, col5, col6 = st.columns(3)
    with col4:
        genetical_risk = st.number_input('Genetical Risk (0–5)', min_value=0, max_value=5, step=1)
    with col5:
        insurance_plan = st.selectbox('Insurance Plan', ['Bronze', 'Silver', 'Gold'])
    with col6:
        employment_status = st.selectbox('Employment Status', ['Salaried', 'Self-Employed', 'Freelancer', ''])

    st.subheader("🧬 Personal Details")
    col7, col8, col9 = st.columns(3)
    with col7:
        gender = st.selectbox('Gender', ['Male', 'Female'])
    with col8:
        marital_status = st.selectbox('Marital Status', ['Unmarried', 'Married'])
    with col9:
        bmi_category = st.selectbox('BMI Category', ['Normal', 'Obesity', 'Overweight', 'Underweight'])

    st.subheader("🚬 Habits & Region")
    col10, col11, col12 = st.columns(3)
    with col10:
        smoking_status = st.selectbox('Smoking Status', ['No Smoking', 'Regular', 'Occasional'])
    with col11:
        region = st.selectbox('Region', ['Northwest', 'Southeast', 'Northeast', 'Southwest'])
    with col12:
        medical_history = st.selectbox('Medical History', [
            'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
            'Thyroid', 'Heart disease', 'High blood pressure & Heart disease', 
            'Diabetes & Thyroid', 'Diabetes & Heart disease'
        ])

    # Submit button
    submitted = st.form_submit_button("💰 Predict Premium")

    if submitted:
        if employment_status == '':
            st.warning("⚠️ Please select all fields before predicting.")
        else:
            with st.spinner("🔄 Calculating your premium..."):
                input_dict = {
                    'Age': age,
                    'Number of Dependants': number_of_dependants,
                    'Income in Lakhs': income_lakhs,
                    'Genetical Risk': genetical_risk,
                    'Insurance Plan': insurance_plan,
                    'Employment Status': employment_status,
                    'Gender': gender,
                    'Marital Status': marital_status,
                    'BMI Category': bmi_category,
                    'Smoking Status': smoking_status,
                    'Region': region,
                    'Medical History': medical_history
                }

                prediction = predict(input_dict)

                # Enhanced premium display
                button_bg = "#144272"
                highlight_bg = "#DDF2FD"
                text_color = "#0A2647"

                st.markdown(f"""
                    <div style="border: 2px solid {button_bg}; border-radius: 15px; padding: 1rem; background-color: {highlight_bg}; text-align: center;">
                        <h3 style="color:{text_color}; margin-bottom: 10px;">✅ Your Estimated Health Insurance Cost:</h3>
                        <h1 style="color:{text_color}; font-size: 3rem;">₹{prediction}</h1>
                    </div>
                """, unsafe_allow_html=True)

                st.balloons()
