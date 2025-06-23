from gtts import gTTS
import os
from uuid import uuid4

def generate_audio(text: str, lang="en") -> str:
    filename = f"{uuid4()}.mp3"
    tts = gTTS(text=text, lang=lang)
    path = f"src/outputs/{filename}"
    tts.save(path)
    return path, filename
