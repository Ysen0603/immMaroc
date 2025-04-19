import os
import google.generativeai as genai
from dotenv import load_dotenv
from src.processing import process_car_images

def main():
    """Loads environment variables, configures the API, and starts processing."""
    load_dotenv()  # Load environment variables from .env file

    api_key = os.environ.get('GENAI_API_KEY')
    if not api_key:
        print("Error: GENAI_API_KEY not found in environment variables.")
        print("Please ensure you have a .env file with GENAI_API_KEY='your_api_key'")
        return

    try:
        genai.configure(api_key=api_key)
        print("Gemini API configured successfully.")
    except Exception as e:
        print(f"Error configuring Gemini API: {e}")
        return

    # Define the folder containing car images (relative to main.py)
    cars_folder = 'cars'
    process_car_images(cars_folder)

if __name__ == "__main__":
    main()
