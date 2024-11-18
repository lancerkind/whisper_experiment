from openai import OpenAI
from typing import Any, Dict
import json

def load_glossary()-> Dict[str, str]: 
  with open("phonetic_glossary.json", "r") as f:
    data = json.load(f)
  return data

glossary = load_glossary()
glossary_prompt = "You are a highly paid copy editor who corrects audio to text transcriptions. This audio podcast is an interview with Lance Kind and guest Richard Hundhausen. Please ensure these key terms are spelled correctly by revising the text: " + ", ".join([f"{term} ({phonetic})" for term, phonetic in glossary.items()])

def correct_transcript(transcript_filename: str, glossary_prompt: str) -> str :
  client = OpenAI()

  with open(transcript_filename, "r") as f:
    transcript = json.load(f)

  editor_response = client.chat.completions.create(
      model="gpt-4o",
      temperature=0.5,
      messages=[
          {
              "role": "system",
              "content": glossary_prompt
          },
          {
              "role": "user",
              "content": transcript['text']
          }
      ]
  )
  return editor_response.choices[0].message.content

corrected_text = correct_transcript("transcript_test_after_silence_no_music.json", glossary_prompt)
print(corrected_text)