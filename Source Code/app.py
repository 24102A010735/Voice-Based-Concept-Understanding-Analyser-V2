import streamlit as st
from src.speech_to_text import SpeechToText
from src.semantic_analysis import SemanticAnalyzer
from src.audio_features import AudioFeatures

# MUST be the first Streamlit command
st.set_page_config(
    page_title="Voice-Based Concept Understanding Analyser",
    page_icon="🎤",
    layout="wide"
)

st.write("✅ APP VERSION: Audio Analysis V1")

st.title("🎤 Voice-Based Concept Understanding Analyser")

st.write("Upload your voice explanation and let AI evaluate your understanding.")

# -----------------------------
# Topic Selection
# -----------------------------
topic = st.selectbox(
    "Select Topic",
    [
        "Artificial Intelligence",
        "Machine Learning",
        "Cloud Computing",
        "Data Science"
    ]
)

# -----------------------------
# Audio Upload
# -----------------------------
audio = st.file_uploader(
    "Upload Audio",
    type=["wav", "mp3", "m4a"]
)

if audio is not None:

    st.audio(audio)

    if st.button("Analyze"):

        with st.spinner("Analyzing your explanation..."):

            # -----------------------------
            # Speech-to-Text
            # -----------------------------
            stt = SpeechToText()
            transcript, audio_path = stt.transcribe_audio(audio)

            # -----------------------------
            # Semantic Analysis
            # -----------------------------
            semantic = SemanticAnalyzer()
            score, feedback = semantic.analyze(
                topic,
                transcript
            )

            # -----------------------------
            # Audio Feature Analysis
            # -----------------------------
            audio_analysis = AudioFeatures()
            features = audio_analysis.analyze(
                audio_path,
                transcript
            )

            # DEBUG
            st.write("### DEBUG")
            st.write(features)

        st.success("Analysis Complete!")

        # -----------------------------
        # Transcript
        # -----------------------------
        st.subheader("📝 Transcript")
        st.write(transcript)

        # -----------------------------
        # Semantic Analysis
        # -----------------------------
        st.subheader("🧠 Semantic Analysis")

        st.metric(
            label="Similarity Score",
            value=f"{score}%"
        )

        st.success(feedback)

        # -----------------------------
        # Audio Analysis
        # -----------------------------
        st.subheader("🎙 Audio Analysis")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Duration",
                f"{features['duration']} sec"
            )

            st.metric(
                "Words Per Minute",
                features["wpm"]
            )

            st.metric(
                "Pause Ratio",
                f"{features['pause_ratio']} %"
            )

        with col2:

            st.metric(
                "Voice Energy",
                features["energy"]
            )

            st.metric(
                "Filler Words",
                features["filler_count"]
            )