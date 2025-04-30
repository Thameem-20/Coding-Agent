# Simple AI Agent using Gemini API

This is a simple AI agent implementation using Google's Gemini API.

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Get your Gemini API key:
   - Go to https://makersuite.google.com/app/apikey
   - Create a new API key

3. Create a `.env` file in the project root and add your API key:
```
GEMINI_API_KEY=your_api_key_here
```

## Usage

Run the agent:
```bash
python ai_agent.py
```

The agent will start a conversation with you. Type 'quit' to exit the conversation.

## Features

- Simple command-line interface
- Error handling for API issues
- Easy to extend and modify 