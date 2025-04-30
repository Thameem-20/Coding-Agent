import os
import google.generativeai as genai
from dotenv import load_dotenv

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

def chat_with_agent():
    print("Welcome to CodeHelper - Your AI Programming Assistant!")
    print("I can help you with:")
    print("- Writing and reviewing code")
    print("- Debugging issues")
    print("- Explaining programming concepts")
    print("- Suggesting best practices")
    print("- Answering technical questions")
    print("\nType 'quit' to exit or 'help' to see available commands.")
    
    while True:
        user_input = input("\nYou: ")
        
        if user_input.lower() == 'quit':
            print("Goodbye! Happy coding!")
            break
        elif user_input.lower() == 'help':
            print("\nAvailable commands:")
            print("- 'quit': Exit the program")
            print("- 'help': Show this help message")
            print("- 'review': Ask for code review")
            print("- 'explain': Get explanation of a concept")
            print("- 'debug': Get help with debugging")
            continue
            
        try:
            # Add context to the prompt
            prompt = f"""You are CodeHelper, a helpful AI programming assistant. 
            Your task is to help with programming-related questions and tasks.
            Be concise, clear, and provide practical solutions.
            If the user asks about code, provide complete, working examples.
            If they need debugging help, ask for relevant code and error messages.
            
            User question: {user_input}
            
            Please provide a helpful response:"""
            
            # Generate response
            response = model.generate_content(prompt)
            print("\nCodeHelper:", response.text)
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            print("Please check your API key and make sure it's valid")

if __name__ == "__main__":
    chat_with_agent() 