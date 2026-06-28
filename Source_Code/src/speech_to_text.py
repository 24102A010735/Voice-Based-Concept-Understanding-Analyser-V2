import whisper
import tempfile
import os

class SpeechToText:

    def __init__(self):
        print("Loading Whisper model...")
        self.model = whisper.load_model("tiny")
        print("Whisper model loaded.")

    def transcribe_audio(self, uploaded_file):

        suffix = os.path.splitext(uploaded_file.name)[1]

        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(uploaded_file.read())
            audio_path = tmp.name

        print("Temporary file:", audio_path)

        print("Starting transcription...")

        result = self.model.transcribe(audio_path)

        print("Finished transcription.")

        return result["text"], audio_path