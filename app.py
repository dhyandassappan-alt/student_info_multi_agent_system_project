import streamlit as st
import asyncio
import json

from agents.research_agent import research_student
from agents.writer_agent import create_report
from agents.reviewer_agent import review_report


# Page Configuration

st.set_page_config(
    page_title="Student Information Multi-Agent System",
    layout="centered"
)

# Sidebar

with st.sidebar:

    st.title("Project Info")

    st.success("Developer")
    st.write("Dhyan C Dassappan")

    st.info("College")
    st.write("Don Bosco College, Panjim")

    st.warning("Technology Used")

    st.write("""
- Python
- FastMCP
-  Multi-Agent System
-  Streamlit
""")

# Title

st.title("Student Information Multi-Agent System")
st.write("Search for a student using your Multi-Agent MCP Project.")

# Metrics

col1, col2, col3 = st.columns(3)

col1.metric(" Students", "6")
col2.metric(" Agents", "3")
col3.metric(" Status", "Active")

st.divider()

# Search Box

student_name = st.text_input("Enter Student Name")

if st.button("Search"):

    if student_name.strip():

        # Research Agent

        st.subheader("Research Agent")

        with st.spinner("Research Agent is searching..."):

            data = asyncio.run(research_student(student_name))

        if "not found" in data.lower():

            st.error("Student Not Found")
            st.stop()

        st.success("Student Found!")

        # Display JSON nicely
        try:
            st.json(json.loads(data))
        except:
            st.code(data)

        # Writer Agent

        st.subheader("Writer Agent")

        report = create_report(data)

        st.code(report)

        # Reviewer Agent

        st.subheader("Reviewer Agent")

        review_report(report)

        st.success("Report Approved!")

        # Celebration

        st.success("Project Completed Successfully!")
        st.balloons()

    else:

        st.warning("Please enter a student name.")

# Footer

st.divider()

st.caption(
    "Built by Dhyan C Dassappan using Python • FastMCP • Streamlit • Multi-Agent Architecture"
)