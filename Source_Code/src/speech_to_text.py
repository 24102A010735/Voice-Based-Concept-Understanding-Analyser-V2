import whisper
import tempfile
import os
import time

class SpeechToText:

    def __init__(self):
        print("STEP 1")
        start = time.time()

        self.model = whisper.load_model("tiny")

        print("STEP 2")
        print("Loaded in", time.time() - start, "seconds")

    def transcribe_audio(self, uploaded_file):

        print("STEP 3")

        suffix = os.path.splitext(uploaded_file.name)[1]

        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(uploaded_file.read())
            audio_path = tmp.name

        print("STEP 4")

        result = self.model.transcribe(audio_path)

        print("STEP 5")

        return result["text"], audio_path