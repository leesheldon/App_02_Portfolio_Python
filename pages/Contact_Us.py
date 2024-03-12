import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    email_title = st.text_input("Email Title")
    raw_message = st.text_area("Your message", max_chars=1000)
    button = st.form_submit_button("Submit")
    if button:
        send_email(user_email, email_title, raw_message)
        st.info("Your email was sent successfully.")

