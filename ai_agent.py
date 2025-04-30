import os
import google.generativeai as genai
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
import markdown
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

# Load environment variables
load_dotenv()

# Get the API key from environment variables
api_key = os.getenv('GEMINI_API_KEY')
if not api_key:
    print("Error: GEMINI_API_KEY not found in .env file")
    print("Please create a .env file with your Gemini API key")
    print("Format: GEMINI_API_KEY=your_api_key_here")
    exit(1)

# Configure the Gemini API
genai.configure(api_key=api_key)

# Initialize the model
model = genai.GenerativeModel('gemini-2.0-flash')

# Initialize Flask app
app = Flask(__name__)

def format_code_blocks(text):
    """Format code blocks with syntax highlighting and proper markdown."""
    lines = text.split('\n')
    formatted_lines = []
    in_code_block = False
    current_language = ''
    current_code = []
    
    for line in lines:
        if line.startswith('```'):
            if in_code_block:
                # End of code block
                code_str = '\n'.join(current_code)
                formatted_lines.append(f'```{current_language}\n{code_str}\n```')
                in_code_block = False
                current_code = []
            else:
                # Start of code block
                in_code_block = True
                current_language = line[3:].strip() or ''
        elif in_code_block:
            current_code.append(line)
        else:
            formatted_lines.append(line)
    # If code block was not closed
    if in_code_block and current_code:
        code_str = '\n'.join(current_code)
        formatted_lines.append(f'```{current_language}\n{code_str}\n```')
    return '\n'.join(formatted_lines)

def get_ai_response(user_input):
    try:
        # Add context to the prompt
        prompt = f"""You are CodeHelper, a specialized AI programming assistant. Your primary role is to provide working code examples and solutions.

When responding to any programming-related question:
1. ALWAYS include a complete, working code example
2. Use markdown code blocks with the correct language specification
3. Format the code properly with indentation
4. Add comments to explain complex parts
5. Include a brief explanation of how the code works
6. If the question is about a specific language or framework, use that language/framework in your example

If the user asks for:
- A specific algorithm or data structure: Provide a complete implementation
- A programming concept: Explain with a practical code example
- Debugging help: Ask for their code and provide a fixed version
- Best practices: Show examples of good and bad code
- A feature implementation: Provide a complete working solution

For code examples:
- Use clear, descriptive variable names
- Include necessary imports
- Add error handling where appropriate
- Include comments for complex logic
- Show both the code and its expected output

User question: {user_input}

Please provide a complete, working code example with explanation:"""
        
        # Generate response
        response = model.generate_content(prompt)
        # Format the response with markdown and code highlighting
        formatted_response = format_code_blocks(response.text)
        return formatted_response
    except Exception as e:
        return f"An error occurred: {str(e)}"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    response = get_ai_response(user_message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True) 