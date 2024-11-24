import argparse
from openai import OpenAI

def transcribe(path_to_mp3: str) -> str:
    """Transcribe an mp3 to a string"""
    client = OpenAI()
    audio_file= open(path_to_mp3, "rb")
    transcription = client.audio.transcriptions.create(
      model="whisper-1",
      file=audio_file
    )
    return transcription.text

def main():
    parser = argparse.ArgumentParser(description="Transcribe a given mp3 file to text and print transcript to screen.\nTranscription accuracy is low.")
    parser.add_argument("path_to_mp3", type=str, help="The path to the mp3 file to be transcribed.")
    args = parser.parse_args()
    transcription = transcribe(args.path_to_mp3)
    print(transcription)
    
if __name__ == "__main__":
    main()