import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Ardit Sulce")
    content = """
    I am Ly Han Co. I have worked 5 years as Software Engineer at DI Central Corporation and 3 years as System Analyst at Bayer Vietnam. So I have experienced in using some software such as ERP (SAP), SQL Server, C#, .Net, CRM. Besides, I have experienced in develop applications and tools for different departments included accountant, human resources, financial and production and also help them to increase overall efficiency by reducing the time and capital invested in ERP systems.
    """
    st.info(content)
