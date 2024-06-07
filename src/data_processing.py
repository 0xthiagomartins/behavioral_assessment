import streamlit as st


def validate_inputs(attention_span, social_interaction, activity_level):
    if not (0 <= attention_span <= 180):
        st.error("Attention Span must be between 0 and 180 minutes.")
        return False
    if social_interaction not in ["Low", "Medium", "High"]:
        st.error("Social Interaction Level must be Low, Medium, or High.")
        return False
    if not (1 <= activity_level <= 10):
        st.error("Activity Level must be between 1 and 10.")
        return False
    return True
