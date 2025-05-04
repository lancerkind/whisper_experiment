import argparse
from openai import OpenAI
from pydub import AudioSegment

def transcribe_singlepass(path_to_mp3: str) -> str:
    """Transcribes an entire mp3 to a character string of so-so quality."""

    client = OpenAI()
    audio_file= open(path_to_mp3, "rb")
    transcription = client.audio.transcriptions.create(
      model="whisper-1",
      file=audio_file
    )
    return transcription.text

def transcribe_segments(segments) -> str:
    """Transcribes segments of an mp3 to a character string."""

    transcript_parts = []
    temp_mp3_filename = "temp_segment.mp3"

    for segment in segments:
        segment.export(temp_mp3_filename, format="mp3")
        client = OpenAI()
        with open(temp_mp3_filename, "rb") as audio_file: 
            transcribed_segment = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )
        transcript_parts.append(transcribed_segment.text)

    # Clean up the temporary file
    import os
    os.remove(temp_mp3_filename)   

    return "".join(transcript_parts)

def segment_audio(file_path, segment_duration_s=8*60):
    """ segment audio so that the Whisper API doesn't hit it's limit"""
    audio = AudioSegment.from_mp3(file_path)
    segments = []
    for i in range(0, len(audio), segment_duration_s * 1000):
        segments.append(audio[i:i + segment_duration_s * 1000])
    return segments

def main():
    parser = argparse.ArgumentParser(description="Transcribe a given mp3 file to text and print transcript to screen.\nTranscription accuracy is low.")
    parser.add_argument("path_to_mp3", type=str, help="The path to the mp3 file to be transcribed.")
    args = parser.parse_args()
#    transcription = transcribe(args.path_to_mp3)
    segments = segment_audio(args.path_to_mp3, 20*60)
    transcription = transcribe_segments(segments)
    print(transcription)
    
if __name__ == "__main__":
    main()