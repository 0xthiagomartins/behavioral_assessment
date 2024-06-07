import streamlit as st


def display_summary(result):
    st.subheader("Summary")
    st.write("### Detailed Assessment Report")
    st.write(f"**Attention Span:** {result['Attention Span']} minutes")
    st.write(f"**Social Interaction Level:** {result['Social Interaction Level']}")
    st.write(f"**Activity Level:** {result['Activity Level']}")
    st.write(f"**Risk Score:** {result['Risk Score']}")
    st.write(f"**Risk Level:** {result['Risk Level']}")
    st.success("Report generated successfully!")
