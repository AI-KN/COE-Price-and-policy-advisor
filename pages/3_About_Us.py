import streamlit as st

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="My Streamlit App"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("Project Scope: Understanding COE in Singapore")

st.write("This app aims to achieve 2 purposes:")
'''
1) Leverage RAG to help users better understand COE-related matters, and
2) Customised filters and data visualisation that allows users to explore COE data for better decision making.
'''
'''
Data sources:

Intent and common answers to common questions relating to COE - https://www.mot.gov.sg/news/Details/oral-reply-by-acting-minister-for-transport-chee-hong-tat-to-parliamentary-question-on-coe-demand-and-supply

General COE info - https://onemotoring.lta.gov.sg/content/onemotoring/home/buying/upfront-vehicle-costs/certificate-of-entitlement--coe-.html

History of COE - https://www.nlb.gov.sg/main/article-detail?cmsuuid=9fadc994-c8b2-45a9-9f35-372d05703ddc

Detailed explanation of COE Bidding and calculation - https://blog.seedly.sg/coe-bidding-and-price-history-trend-singapore/

Data for COE History - https://data.gov.sg/datasets/d_69b3380ad7e51aff3a7dcc84eba52b8a/view
'''

