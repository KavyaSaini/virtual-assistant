# Updated Python Virtual Assistant

## Features
- Greeting, date and time
- Opens Google, YouTube and Gmail
- Google web search
- Wikipedia summaries
- Built-in answers for a few common questions
- Automatically tries Wikipedia when an unrecognized question is typed
- Save and read notes

## Install on macOS
Open Terminal in this folder and run:

```bash
python3 -m pip install -r requirements.txt
python3 virtual_assistant.py
```

## Install on Windows
Open Command Prompt in this folder and run:

```bash
py -m pip install -r requirements.txt
py virtual_assistant.py
```

## Example questions
- capital of india
- what is AI
- who is APJ Abdul Kalam
- who is Albert Einstein
- search machine learning
- wikipedia neural network

The assistant uses a small built-in answer list for a few common questions. For other questions, it tries to fetch a Wikipedia summary. An internet connection is required for Wikipedia and web search.
