import streamlit as st
from business import DISC

st.title("DISC Personality Test")

disc = DISC()
questions = disc.questions

answers = []
for i, question in enumerate(questions):
    answer = st.radio(
        f"Q{i+1}: {question}",
        options=["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"],
        key=i,
    )
    answers.append(answer)

if st.button("Submit"):
    if any(answer == "" for answer in answers):
        st.warning("Please answer all the questions.")
    else:
        scores = disc.calculate_scores(answers)
        personality = disc.classify_personality(scores)
        description = disc.get_personality_description(personality)
        st.write(f"Your DISC personality type is: {personality}")
        st.write(description)

        graph_path = disc.plot_disc_graph(scores)
        st.image(graph_path, caption="DISC Personality Graph")
