from openai import OpenAI
from typing import Any, Dict
import json

def load_glossary()-> Dict[str, str]: 
  with open("phonetic_glossary.json", "r") as f:
    data = json.load(f)
  return data

glossary = load_glossary()
glossary_prompt = "This audio podcast is an interview with Lance Kind and guest Richard Hundhausen. Key terms: " + ", ".join([f"{term} ({phonetic})" for term, phonetic in glossary.items()])

def create_transcription(filename: str, glossary_prompt: str) -> Dict[str, str] :
  client = OpenAI()
  audio_file= open(filename, "rb")
  print("using this prompt: " + glossary_prompt)
  transcription = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file,
    prompt=glossary_prompt
  )
  return transcription

transcription = create_transcription("/Users/lancer/Desktop/030 Nexus for multi-team Scrum, with Richard Hundhausen_silence&Music removed.mp3", glossary_prompt)
print(transcription.text)