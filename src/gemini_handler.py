import datetime
import google.generativeai as genai
import os
import PIL.Image
import time
from src.utils.validation import is_valid_immatriculation

# Note: genai.configure should be called in the main script after loading env vars.

def gemini_response_with_retry(prompt, image_path, max_retries=3):
    """Generates content using Gemini with retry mechanism."""
    try:
        img = PIL.Image.open(image_path)
    except FileNotFoundError:
        return {
            "error": f"Image file not found at: {image_path}",
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
    except Exception as e:
        return {
            "error": f"Error opening image: {e}",
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

    # Ensure the model name is correct, e.g., 'gemini-1.5-flash' or similar
    # Using 'gemini-pro-vision' as a common example for image input
    # Adjust 'gemini-2.0-flash' if that's the specific model you intend to use
    # model = genai.GenerativeModel('gemini-pro-vision')
    model = genai.GenerativeModel('gemini-1.5-flash') # Using a known valid model name

    for attempt in range(max_retries):
        try:
            response = model.generate_content([prompt, img])
            # Accessing response text safely
            response_text = ""
            if response.parts:
                 # Assuming the text is in the first part for vision models
                 response_text = response.parts[0].text
            elif hasattr(response, 'text'):
                 response_text = response.text # Fallback for other response structures

            if is_valid_immatriculation(response_text):
                return {
                    "response": response_text,
                    "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                }

            print(f"Attempt {attempt + 1}: Invalid format - '{response_text}'")
            if attempt < max_retries - 1:
                time.sleep(5)  # Wait before retrying

        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {str(e)}")
            if attempt < max_retries - 1:
                time.sleep(5)

    # Return error if all retries fail or format is invalid
    return {
        "error": "Invalid format or failed after retries",
        "response": "Invalid format after retries", # Keep original message for context
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
