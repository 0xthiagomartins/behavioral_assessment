import streamlit as st
from data_processing import validate_inputs
from business_logic import assess_behavior
from ui import display_summary


def main():
    st.title("Behavioral Assessment Application")

    st.header("Input Behavioral Metrics")
    attention_span = st.number_input(
        "Attention Span (minutes)", min_value=0, max_value=180, value=60
    )
    social_interaction = st.selectbox(
        "Social Interaction Level", ["Low", "Medium", "High"]
    )
    activity_level = st.slider("Activity Level", 1, 10, 5)

    if st.button("Generate Report"):
        if validate_inputs(attention_span, social_interaction, activity_level):
            result = assess_behavior(attention_span, social_interaction, activity_level)
            display_summary(result)


if __name__ == "__main__":
    main()
