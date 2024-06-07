import streamlit as st


def display_summary(result):
    st.subheader("Summary")
    st.write(result)
    st.success("Report generated successfully!")
