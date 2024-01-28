import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
class GeminiChat:
    def __init__(self):
        # Retrieve the API key from an environment variable
        api_key = GOOGLE_API_KEY
        if not api_key:
            raise ValueError("Google API key not found in environment variables.")

        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')

    def send_message(self, prompt, temp=0.42, top_p=1.0):
        """
        Send a message to the Gemini model with specified temperature and top probability.
        """
        try:
            generation_config = genai.types.GenerationConfig(temperature=temp, top_p=top_p)
            response = self.model.generate_content(prompt, generation_config=generation_config)
            return response.text.strip()
        except Exception as e:
            print(f"Error in generating response: {e}")
            return None

# Example usage
if __name__ == "__main__":
    gemini_chat = GeminiChat()
    response = gemini_chat.send_message("Hello, Gemini! How are you today?", temp=0.7, top_p=0.9)
    if response:
        print("Gemini's response:", response)
    else:
        print("Failed to get response from Gemini.")
