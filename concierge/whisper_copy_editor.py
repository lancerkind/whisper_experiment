import json
import argparse
from typing import Any, Dict
from openai import OpenAI

""" 
Podcast context contains information about the podcast from the tags and show notes and is used to
correct phonetic spelling errors.
"""
def load_podcast_context(filename: str)-> str:
    with open(filename, "r") as f:
        data = f.read()
    return data

def correct_transcript(transcript_filename: str, podcast_context: str) -> str :
    client = OpenAI()
    glossary_prompt: str = "You're role is as a highly paid copy editor. The transcript I'm giving you has phonetic errors. Use this sample text to correct the spelling of guest names and terms used in the podcast: " + podcast_context
    
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
    parser.add_argument("transcriptFilename", type=str, help="The file name of the transcript to be corrected.")
    parser.add_argument("podcastContext", type=str, help="The file name of the phonetic dictionary to be used by the editor.")
    args = parser.parse_args()

    podcastContext: str = load_podcast_context(args.podcastContext)
    correctedText: str = correct_transcript(args.transcriptFilename, podcastContext)
    print(correctedText)

if __name__ == "__main__":
    main()