from google import genai
from google.genai import types
import tempfile
import os

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

class SpeechToText:

    def transcribe_audio(self, uploaded_file):

        suffix = os.path.splitext(uploaded_file.name)[1]

        mime_map = {
            ".wav": "audio/wav",
            ".mp3": "audio/mpeg",
            ".m4a": "audio/mp4"
        }

        mime_type = mime_map.get(suffix.lower(), "audio/wav")

        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(uploaded_file.read())
            audio_path = tmp.name

        with open(audio_path, "rb") as f:
            audio_bytes = f.read()

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[
                types.Part.from_bytes(
                    data=audio_bytes,
                    mime_type=mime_type,
                ),
                "Transcribe this audio exactly. Return only the transcript."
            ],
        )

        return response.text.strip(), audio_path