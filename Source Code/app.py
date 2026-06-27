import streamlit as st
from src.speech_to_text import SpeechToText
from src.semantic_analysis import SemanticAnalyzer

st.set_page_config(
    page_title="Voice-Based Concept Understanding Analyser",
    page_icon="🎤"
)

st.title("🎤 Voice-Based Concept Understanding Analyser")

topic = st.selectbox(
    "Select Topic",
    [
        "Artificial Intelligence",
        "Machine Learning",
        "Cloud Computing",
        "Data Science"
    ]
)

audio = st.file_uploader(
    "Upload Audio",
    type=["wav", "mp3", "m4a"]
)

if audio is not None:

    st.audio(audio)

    if st.button("Analyze"):

        with st.spinner("Analyzing..."):

            stt = SpeechToText()
            transcript, audio_path = stt.transcribe_audio(audio)

            semantic = SemanticAnalyzer()
            score, feedback = semantic.analyze(
                topic,
                transcript
            )

        st.success("Analysis Complete!")

        st.subheader("📝 Transcript")
        st.write(transcript)

        st.subheader("🧠 Semantic Analysis")

        st.metric(
            "Similarity Score",
            f"{score}%"
        )

        st.success(feedback)