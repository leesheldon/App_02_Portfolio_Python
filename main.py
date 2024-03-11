import streamlit as st
import pandas

st.set_page_config()

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Ly Han Co")
    content = """
    Hi, I am Ly Han Co. I have worked 5 years as Software Engineer at DI Central and 3 years as System Analyst at Bayer Vietnam. My technical skills are SQL Server, C# .NET, CRM, Power Apps and Power BI in applications support for different Accounting, Human resources, Financial and Production teams. This helped them to increase overall efficiency by reducing the time and capital invested in ERP systems.
    """
    st.info(content)

content2 = """
Below you can find some of the apps which I have built in Python. Feel free to contact me!
"""
st.write(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])

















