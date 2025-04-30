# Coding Agent

A simple AI-powered coding assistant using Google's Gemini API, with a modern web interface.

## Features

- Modern web chat interface (Flask + HTML/CSS/JS)
- Supports markdown and syntax-highlighted code blocks
- Focused on providing complete, working code examples
- Error handling for API issues
- Easy to extend and modify
- Footer with author credit and GitHub link

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Thameem-20/Coding-Agent.git
   cd Coding-Agent
   ```

2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Get your Gemini API key:**
   - Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key

4. **Create a `.env` file in the project root and add your API key:**
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## Usage

1. **Run the agent:**
   ```bash
   python ai_agent.py
   ```
2. **Open your browser and go to:**
   ```
   http://localhost:5000
   ```

## Example Questions
- "Show me how to implement a binary search in Python."
- "Write a function to reverse a string in JavaScript."
- "Create a simple REST API using Flask."

## Demo
![Web UI Screenshot](screenshot.png)

## Credits

Built by Thameem — [GitHub](https://github.com/Thameem-20/Coding-Agent) 