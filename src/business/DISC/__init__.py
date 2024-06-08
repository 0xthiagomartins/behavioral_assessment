import json, os
import matplotlib.pyplot as plt
import numpy as np
import tempfile


class DISC:
    def __init__(self):
        self.questions, self.trait_mapping = self._load_questions_and_traits(
            "src/business/DISC/data/questions.json"
        )

    def _load_questions_and_traits(self, path):
        with open(path, "r") as file:
            data = json.load(file)
            return data["questions"], data["trait_mapping"]

    def calculate_scores(self, answers):
        scores = {"D": 0, "I": 0, "S": 0, "C": 0}
        for i, answer in enumerate(answers):
            trait = self.trait_mapping[str(i)]
            if answer == "Strongly Agree":
                scores[trait] += 4
            elif answer == "Agree":
                scores[trait] += 3
            elif answer == "Neutral":
                scores[trait] += 2
            elif answer == "Disagree":
                scores[trait] += 1
            elif answer == "Strongly Disagree":
                scores[trait] += 0
        return scores

    def classify_personality(self, scores):
        max_score = max(scores, key=scores.get)
        return max_score

    def get_personality_description(self, personality_type):
        descriptions = {
            "D": "Dominance: People with high dominance are confident and like to take control.",
            "I": "Influence: People with high influence are persuasive and enjoy social interactions.",
            "S": "Steadiness: People with high steadiness are patient and prefer a stable environment.",
            "C": "Conscientiousness: People with high conscientiousness value accuracy and prefer working with details.",
        }
        return descriptions.get(personality_type, "Unknown personality type.")

    def plot_disc_graph(self, scores):
        categories = ["D", "I", "S", "C"]
        values = [scores[cat] for cat in categories]

        angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
        values += values[:1]
        angles += angles[:1]

        fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
        ax.fill(angles, values, color="blue", alpha=0.25)
        ax.plot(angles, values, color="blue", linewidth=2)
        ax.set_yticklabels([])
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(categories)
        plt.title("DISC Personality Graph")

        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp_file:
            plt.savefig(tmp_file.name)
            plt.close()
            return tmp_file.name
