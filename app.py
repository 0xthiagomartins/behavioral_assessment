# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def main():
    st.title("Behavioral Assessment Application")

    st.header("Input Behavioral Metrics")

    attention_span = st.slider("Attention Span (minutes)", 0, 60, 30)
    social_interaction = st.selectbox(
        "Social Interaction Level", ["Low", "Medium", "High"]
    )
    activity_level = st.number_input("Activity Level (1-10)", 1, 10, 5)

    st.header("Summary of Inputs")
    st.write(f"Attention Span: {attention_span} minutes")
    st.write(f"Social Interaction Level: {social_interaction}")
    st.write(f"Activity Level: {activity_level}")

    st.header("Visualizations")

    # Convert social interaction level to numerical values for visualization
    social_interaction_map = {"Low": 1, "Medium": 2, "High": 3}
    social_interaction_num = social_interaction_map[social_interaction]

    metrics = {
        "Attention Span (minutes)": attention_span,
        "Social Interaction Level": social_interaction_num,
        "Activity Level": activity_level,
    }

    df = pd.DataFrame(list(metrics.items()), columns=["Metric", "Value"])

    fig, ax = plt.subplots()
    ax.bar(df["Metric"], df["Value"], color=["blue", "green", "red"])
    ax.set_xticks(df.index)
    ax.set_xticklabels(df["Metric"], rotation=45)
    st.pyplot(fig)

    if st.button("Generate Report"):
        st.write(
            "Report Generated. Thank you for using the Behavioral Assessment Application."
        )


if __name__ == "__main__":
    main()
