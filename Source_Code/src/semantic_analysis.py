import json
import streamlit as st
from sentence_transformers import SentenceTransformer, util

@st.cache_resource
def load_semantic_model():
    print("Downloading model...")
    model = SentenceTransformer("all-MiniLM-L6-v2")
    print("Model downloaded.")
    return model

class SemanticAnalyzer:

    def __init__(self):

        print("Inside SemanticAnalyzer")

        self.model = load_semantic_model()

        print("Opening JSON")

        with open("data/reference_concepts.json","r",encoding="utf-8") as f:
            self.reference = json.load(f)

        print("Semantic Ready")

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
        print("Semantic Analysis Finished")
        return score, feedback