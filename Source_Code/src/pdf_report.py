from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import os


class PDFReport:

    def generate(
        self,
        topic,
        transcript,
        similarity,
        feedback,
        features,
        overall_score,
        grade,
        remark
    ):

        os.makedirs("reports", exist_ok=True)

        filename = f"reports/{topic.replace(' ', '_')}_Report.pdf"

        doc = SimpleDocTemplate(filename)

        styles = getSampleStyleSheet()

        story = []

        story.append(Paragraph("<b>Voice-Based Concept Understanding Analyser</b>", styles["Title"]))

        story.append(Paragraph(f"<b>Topic:</b> {topic}", styles["BodyText"]))

        story.append(Paragraph("<br/>", styles["BodyText"]))

        story.append(Paragraph("<b>Transcript</b>", styles["Heading2"]))

        story.append(Paragraph(transcript, styles["BodyText"]))

        story.append(Paragraph("<br/>", styles["BodyText"]))

        story.append(Paragraph("<b>Semantic Analysis</b>", styles["Heading2"]))

        story.append(Paragraph(f"Similarity Score : {similarity}%", styles["BodyText"]))

        story.append(Paragraph(feedback, styles["BodyText"]))

        story.append(Paragraph("<br/>", styles["BodyText"]))

        story.append(Paragraph("<b>Audio Analysis</b>", styles["Heading2"]))

        story.append(Paragraph(f"Duration : {features['duration']} sec", styles["BodyText"]))
        story.append(Paragraph(f"Words Per Minute : {features['wpm']}", styles["BodyText"]))
        story.append(Paragraph(f"Pause Ratio : {features['pause_ratio']} %", styles["BodyText"]))
        story.append(Paragraph(f"Voice Energy : {features['energy']}", styles["BodyText"]))
        story.append(Paragraph(f"Filler Words : {features['filler_count']}", styles["BodyText"]))

        story.append(Paragraph("<br/>", styles["BodyText"]))

        story.append(Paragraph("<b>Overall AI Evaluation</b>", styles["Heading2"]))

        story.append(Paragraph(f"Overall Score : {overall_score}/100", styles["BodyText"]))
        story.append(Paragraph(f"Grade : {grade}", styles["BodyText"]))
        story.append(Paragraph(f"Recommendation : {remark}", styles["BodyText"]))

        doc.build(story)

        return filename