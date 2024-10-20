# Set up and run this Streamlit App
import streamlit as st
import pandas as pd
# from helper_functions import llm
from helper_functions.utility import check_password
from helper_functions.rag import rag_ans


# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="My COE Advisor 🚗"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("🤖 Your personal COE Advisor")
st.image("logo.jpg", caption="COE Advisor")

# Check if the password is correct.  
if not check_password():  
    st.stop()

form = st.form(key="form")
form.subheader("Hello! I'm your dedicated COE advisor!")

user_prompt = form.text_area("Ask your COE related questions here! I am capable of conversing, so feel free to ask continuous questions.", height=200)

if form.form_submit_button("Submit"):
    
    st.toast(f"Request Submitted - {user_prompt}")

    st.divider()

    response = rag_ans(user_prompt)
    st.write(response)

    #st.divider()

    print(response)
    #df = pd.DataFrame(course_details)
    #df 


with st.expander("Disclaimer"):
    st.write('''
            IMPORTANT NOTICE: This web application is a prototype developed for educational purposes only. The information provided here is NOT intended for real-world usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.

            Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.

            Always consult with qualified professionals for accurate and personalized advice.
    ''')
