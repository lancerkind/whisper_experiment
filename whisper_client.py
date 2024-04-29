from openai import OpenAI
client = OpenAI()

audio_file= open("/Users/lancer/Desktop/030 Nexus for multi-team Scurm, with Richard Hundhausen - 12:28:23, 15.55.mp3", "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)
print(transcription.text)

