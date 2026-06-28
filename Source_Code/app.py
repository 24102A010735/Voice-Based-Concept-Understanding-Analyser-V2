import streamlit as st
from src.speech_to_text import SpeechToText
from src.semantic_analysis import SemanticAnalyzer
from src.audio_features import AudioFeatures
from src.scoring import ScoringEngine
from src.pdf_report import PDFReport
import psutil
import os

st.write(f"RAM Usage: {psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024:.2f} MB")

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Voice-Based Concept Understanding Analyser",
    page_icon="🎤",
    layout="wide"
)
@st.cache_resource
def load_stt():
    return SpeechToText()
# =============================
# Sidebar
# =============================
st.sidebar.title("🎤 Voice Analyser")

st.sidebar.markdown("---")

st.sidebar.info("""
**Version:** 1.0

**Developer:** T. A. Karthik

**Project:** Voice-Based Concept Understanding Analyser

**Technology:**
- Whisper AI
- Sentence Transformers
- Streamlit
- ReportLab
""")

st.sidebar.markdown("---")

st.sidebar.success("Upload your audio and click Analyze.")
# -----------------------------
# Title
# -----------------------------
st.title("🎤 Voice-Based Concept Understanding Analyser")

st.write(
    "Upload your voice explanation and let AI evaluate your conceptual understanding."
)

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

# -----------------------------
# Main Logic
# -----------------------------
if audio is not None:

    st.audio(audio)

    if st.button("Analyze"):

        with st.spinner("Analyzing your explanation..."):

            # -----------------------------
            # Speech to Text
            # -----------------------------
            st.write("Loading Whisper...")
            stt = load_stt()
            st.write("Transcribing...")
            transcript, audio_path = stt.transcribe_audio(audio)
            st.write("Loading semantic model...")
            # -----------------------------
            # Semantic Analysis
            # -----------------------------
            
            semantic = SemanticAnalyzer()
            
            st.write("Calculating similarity...")
            score, feedback = semantic.analyze(
                topic,
                transcript
            )
            st.write("Analyzing audio...")
            # -----------------------------
            # Audio Feature Analysis
            # -----------------------------
            audio_analysis = AudioFeatures()

            features = audio_analysis.analyze(
                audio_path,
                transcript
            )

            # -----------------------------
            # Overall Scoring
            # -----------------------------
            scoring = ScoringEngine()

            overall_score, grade, remark = scoring.calculate(
                score,
                features["wpm"],
                features["pause_ratio"],
                features["filler_count"],
                features["energy"]
            )
            # pdf = PDFReport()

            # pdf_path = pdf.generate(
            #     topic,
            #     transcript,
            #     score,
            #     feedback,
            #     features,
            #     overall_score,
            #     grade,
            #     remark
            # )

        st.success("Analysis Complete!")

        # =============================
        # Transcript
        # =============================
        st.subheader("📝 Transcript")

        with st.expander("View Transcript", expanded=True):
            st.write(transcript)

        # =============================
        # Semantic Analysis
        # =============================
        st.subheader("🧠 Semantic Analysis")

        st.metric(
            "Similarity Score",
            f"{score}%"
        )
        st.progress(min(score / 100, 1.0))

        st.success(feedback)

        # =============================
        # Audio Analysis
        # =============================
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

        # =============================
        # Overall AI Evaluation
        # =============================
        st.subheader("🏆 Overall AI Evaluation")

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Overall Score",
                f"{overall_score}/100"
            )
            st.progress(min(overall_score / 100, 1.0))

        with col2:

            st.metric(
                "Grade",
                grade
            )

        with col3:

            st.metric(
                "Recommendation",
                remark
            )

        # =============================
        # Download PDF Report
        # =============================
        # st.subheader("📄 Download Report")

        # with open(pdf_path, "rb") as file:

        #     st.download_button(
        #         label="📥 Download PDF Report",
        #         data=file,
        #         file_name="Voice_Analysis_Report.pdf",
        #         mime="application/pdf"
        #     )
        st.balloons()

        st.success("🎉 Analysis completed successfully!")