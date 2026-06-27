# 🎤 Voice-Based Concept Understanding Analyser

## 📌 Overview

The Voice-Based Concept Understanding Analyser is an AI-powered application that evaluates a user's understanding of technical concepts through spoken explanations. The system converts speech into text, compares the explanation with a reference concept using semantic similarity, analyzes speech characteristics, calculates an overall score, and generates a downloadable PDF report.

---

## 🚀 Features

* 🎤 Speech-to-Text using OpenAI Whisper
* 🧠 Semantic Similarity Analysis using Sentence Transformers
* 🎙 Audio Feature Analysis
* 📊 Overall AI Evaluation Score
* 📄 Automatic PDF Report Generation
* 💻 Interactive Streamlit Interface

---

## 🛠 Technologies Used

* Python
* Streamlit
* Whisper
* Sentence Transformers
* Librosa
* NumPy
* ReportLab

---

## 📂 Project Structure

```
Source Code/
│
├── app.py
├── data/
├── reports/
├── src/
│   ├── speech_to_text.py
│   ├── semantic_analysis.py
│   ├── audio_features.py
│   ├── scoring.py
│   └── pdf_report.py
```

---

## ▶️ How to Run

1. Install dependencies

```
pip install -r requirements.txt
```

2. Start the application

```
streamlit run app.py
```

3. Upload an audio file.

4. Click **Analyze**.

5. Download the generated PDF report.

---

## 📊 Output

* Transcript
* Semantic Similarity Score
* Audio Analysis
* Overall AI Evaluation
* PDF Report

---

## 👨‍💻 Developer

**T. A. Karthik**

B.Tech – CSE (AI & ML)

Mohan Babu University

---

## 📜 License

This project is developed for educational and internship purposes.
