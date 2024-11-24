import json
import argparse
from typing import Any, Dict
from openai import OpenAI

def load_phonetic_dictionary(filename: str)-> Dict[str, str]:
    with open(filename, "r") as f:
        data = json.load(f)
    return data

def correct_transcript(transcript_filename: str, phonetic_dictionary: Dict[str, str]) -> str :
    client = OpenAI()
    glossary_prompt: str = "You're role is as a highly paid copy editor. The transcript I'm giving you has phonetic errors. Use this sample text to correct the spelling of guest names and terms used in the podcast: " + ", ".join([f"{term} ({phonetic})" for term, phonetic in phonetic_dictionary.items()])
    #glossary_prompt: str = "You're role is as a highly paid copy editor. The transcript I'm giving you has phonetic errors. Use this sample text to correct the spelling of guest names and terms used in the podcast: " + ", ".join([f"{term} ({phonetic})" for term, phonetic in phonetic_dictionary.items()])
    
    with open(transcript_filename, "r") as f:
        transcript = f.read()
    
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
                "content": transcript
            }
        ]
    )
    return editor_response.choices[0].message.content if editor_response.choices[0].message.content is not None else ""

def main():
    parser = argparse.ArgumentParser(description="Correct a given transcript with a given editorial prompt and print the corrected text.")
    parser.add_argument("transcript_filename", type=str, help="The file name of the transcript to be corrected.")
    parser.add_argument("phonetic_dictionary_filename", type=str, help="The file name of the phonetic dictionary to be used by the editor.")
    args = parser.parse_args()

    phonetic_dictionary: Dict[str, str] = load_phonetic_dictionary(args.phonetic_dictionary_filename)
    corrected_text = correct_transcript(args.transcript_filename, phonetic_dictionary)
    print(corrected_text)

if __name__ == "__main__":
    main()