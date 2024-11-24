# whisper_experiment

Doing hypothesis testing with the Whisper OpenAI API.

Hypothesis: Whisper will create high-enough quality text transcripts (with some prompting) to automate the act of converting podcast recordings into text.

# What I want to learn:

- how to handle name spelling by providing context _before_ creating a transcript
  - Result: **It cannot.** Prompting didn't improve transcription. Creating a phonetic word list and prompting didn't improve transcription. What was discovered is that post processing the transcript with the LLM using a phonetic word list did solve the problem.
    - Is a phonetic word list instrumental or can a simple prompt with topic and what the conversation is about get the same results without having to use inference to create a phonetic dictionary?
- can it handle an hour long show
- how large a model will be needed for english to text translation.
  - So far:
