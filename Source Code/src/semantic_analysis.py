from sentence_transformers import SentenceTransformer, util
import json


class SemanticAnalyzer:

    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        with open("data/reference_concepts.json", "r", encoding="utf-8") as file:
            self.reference = json.load(file)

    def analyze(self, topic, transcript):

        reference_text = self.reference[topic]

        embedding1 = self.model.encode(
            reference_text,
            convert_to_tensor=True
        )

        embedding2 = self.model.encode(
            transcript,
            convert_to_tensor=True
        )

        similarity = util.cos_sim(
            embedding1,
            embedding2
        ).item()

        score = round(similarity * 100, 2)

        if score >= 85:
            feedback = "🟢 Excellent Understanding"

        elif score >= 65:
            feedback = "🟡 Moderate Understanding"

        else:
            feedback = "🔴 Poor Understanding"

        return score, feedback