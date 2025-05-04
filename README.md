# whisper_experiment

Doing hypothesis testing with the Whisper OpenAI API.

Hypothesis: Whisper will create high-enough quality text transcripts (with some prompting) to automate the act of converting podcast recordings into text.

# Depedencies
You'll need a paid OpenAI account.
Have your OpenAI key defined in a .env file in whisper_expirement directory.
```
# Once you add your API key below, make sure to not share it with anyone! The API key should remain private.
OPENAI_API_KEY=<insert key here>
```

* Python 3
* OpenAI Whisper 
* ChatGPT 4
* brew install ffmpegffmpe

# What I want to learn:

- how to handle name spelling by providing context _before_ creating a transcript
  - Result: **It cannot.** Prompting didn't improve transcription. Creating a phonetic word list and prompting didn't improve transcription. What was discovered is that post processing the transcript with the LLM using a phonetic word list did solve the problem.
    - Is a phonetic word list instrumental or can a simple prompt with topic and what the conversation is about get the same results without having to use inference to create a phonetic dictionary?
- can it handle an hour long show?
  - Result: An hour show exceeds the size the web api will accept so it will need to be segmented.
- how large a model will be needed for english to text translation?
  - I don't know. As I'm using the whisper over web API, I don't know what size of model they are using as it's not public what "whisper-1" maps to.

# Troubleshooting
- Problem: When running python script, I get:
```
openai.OpenAIError: The api_key client option must be set either by passing api_key to the client or by setting the OPENAI_API_KEY environment variable
```
- Solution 1: Check that you're virtual environment is active: echo $VIRTUAL_ENV
If not, activate the virtual environment: 
```
$ source bin/activate
```
- Solution 2: If virtual environmen is active, I've seen where if I just wait a moment, I can run the script. This leads me to suspect there is something wrong with the network API call.
