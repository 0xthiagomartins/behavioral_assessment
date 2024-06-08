import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def main():
    st.title("Behavioral Assessment Application")

    questions = {
        "You enjoy taking charge of situations": "Dominance",
        "You like to collaborate and work in teams": "Influence",
        "You prefer stability and consistency in your environment": "Steadiness",
        "You pay attention to details and ensure accuracy": "Conscientiousness",
    }

    with st.form(key="behavioral_metrics_form"):
        st.header("Input Behavioral Metrics")
        attention_span = st.number_input(
            "Attention Span (minutes)", min_value=0, max_value=120, step=1
        )
        social_interaction = st.selectbox(
            "Social Interaction Level", ["Low", "Medium", "High"]
        )
        activity_level = st.slider("Activity Level", 1, 10)
        submit_button1 = st.form_submit_button(label="Submit Metrics")

    if submit_button1:
        st.write("### Behavioral Metrics Summary")
        metrics_summary = {
            "Attention Span": attention_span,
            "Social Interaction": social_interaction,
            "Activity Level": activity_level,
        }
        st.write(metrics_summary)


if __name__ == "__main__":
    main()
