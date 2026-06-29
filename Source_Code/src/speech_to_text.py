import whisper
import tempfile
import os
import time

class SpeechToText:

    def __init__(self):
        print("STEP 1 - Before load_model")

        start = time.time()

        self.model = whisper.load_model("tiny")

        print("STEP 2 - After load_model")
        print("Loading Time:", time.time() - start)

    def transcribe_audio(self, uploaded_file):

        print("STEP 3 - Saving Audio")

        suffix = os.path.splitext(uploaded_file.name)[1]

        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(uploaded_file.read())
            audio_path = tmp.name

        print("STEP 4 - Starting Transcription")

        result = self.model.transcribe(audio_path)

        print("STEP 5 - Finished")

        return result["text"], audio_path