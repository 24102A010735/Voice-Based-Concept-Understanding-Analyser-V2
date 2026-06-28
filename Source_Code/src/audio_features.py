import librosa
import numpy as np
import re


class AudioFeatures:

    def analyze(self, audio_path, transcript):

        # Load audio
        y, sr = librosa.load(audio_path, sr=None)

        # Duration
        duration = librosa.get_duration(y=y, sr=sr)

        # RMS Energy
        rms = librosa.feature.rms(y=y)[0]
        average_energy = float(np.mean(rms))

        # Word Count
        words = transcript.split()
        total_words = len(words)

        # Words Per Minute
        if duration > 0:
            wpm = round((total_words / duration) * 60)
        else:
            wpm = 0

        # Filler Words
        fillers = [
            "um",
            "uh",
            "like",
            "you know",
            "actually",
            "basically",
            "so"
        ]

        transcript_lower = transcript.lower()

        filler_count = 0

        for filler in fillers:
            filler_count += len(
                re.findall(r"\b" + re.escape(filler) + r"\b", transcript_lower)
            )

        # Pause Ratio
        pause_ratio = round(
            max(0, (duration - total_words * 0.45) / duration) * 100,
            2
        )

        return {
            "duration": round(duration, 2),
            "energy": round(average_energy, 4),
            "wpm": wpm,
            "filler_count": filler_count,
            "pause_ratio": pause_ratio
        }