import streamlit as st

st.set_page_config(page_title='First app', initial_sidebar_state="expanded")

st.header("Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit")


st.image("redbus.jpg")





x= st.button(" CLICK TO START")
st.balloons()
if x==True:
    st.switch_page("pages/MainPage.py")

   

