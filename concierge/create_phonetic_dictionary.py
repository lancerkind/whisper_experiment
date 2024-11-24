# If not getting intellisense, launch IDE from within environment.
from openai import OpenAI

def generate_phonetics(term):
    client = OpenAI()
    prompt = f"Provide a simple phonetic transcription for the term: {term}. For example, 'Nexus' should be 'NEK-suhs'."
    completion =  client.chat.completions.create(
        model="gpt-4o",
        messages=[
            { "role": "system", "content": "You are a linguistics expert." },
            {
                "role": "user", "content": prompt,
            },
        ],
    )
    return completion.choices[0].message.content.strip()

# List of terms to transcribe phonetically
terms = ["Nexus", "Richard Hundhausen", "Pothi.com", "LeSS", "SaFE", "Scrum", "Agile", "Multi-team Scrum", "Agile Thoughts"]

# Generate phonetic dictionary
phonetic_glossary = {term: generate_phonetics(term) for term in terms}

# Save to JSON
import json
with open("../test_output/phonetic_glossary.json", "w") as f:
    json.dump(phonetic_glossary, f, indent=4)