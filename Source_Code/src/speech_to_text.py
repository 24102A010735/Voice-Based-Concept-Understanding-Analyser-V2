from openai import OpenAI
import tempfile
import os



client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")))


class SpeechToText:

    def transcribe_audio(self, uploaded_file):

        suffix = os.path.splitext(uploaded_file.name)[1]

        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(uploaded_file.read())
            audio_path = tmp.name

        with open(audio_path, "rb") as audio_file:

            transcript = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )

        return transcript.text, audio_path