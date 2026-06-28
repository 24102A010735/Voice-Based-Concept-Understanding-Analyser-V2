import whisper
import tempfile
import os


class SpeechToText:
    def __init__(self):
        # Load Whisper model once
        self.model = whisper.load_model("tiny")

    def transcribe_audio(self, uploaded_file):
        """
        Transcribes uploaded audio using OpenAI Whisper.

        Returns:
            transcript (str)
            audio_path (str)
        """

        suffix = os.path.splitext(uploaded_file.name)[1]

        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(uploaded_file.read())
            audio_path = tmp.name

        result = self.model.transcribe(audio_path)

        return result["text"], audio_path