import os
import time
from src.gemini_handler import gemini_response_with_retry
from src.utils.excel_handler import save_to_excel

def process_car_images(cars_folder='cars'):
    """Process all images in the specified folder and save results to Excel."""
    prompt_text = """The image contains a Moroccan license plate. Its structure is typically: numbers | Arabic letter | numbers.
Please extract only the plate number in this exact format and nothing else the format is: numbers | Arabic letter | numbers.
"""
    # Ensure the cars_folder path is relative to the main script execution directory
    # If main.py is in the root, 'cars' is correct.
    if not os.path.exists(cars_folder):
        print(f"Error: Folder '{cars_folder}' not found relative to the execution directory.")
        return

    image_files = [f for f in os.listdir(cars_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    if not image_files:
        print(f"No images found in the '{cars_folder}' directory.")
        return

    for image_file in image_files:
        image_path = os.path.join(cars_folder, image_file)
        print(f"Processing: {image_file}")

        # Call the Gemini handler
        responses = gemini_response_with_retry(prompt_text, image_path)

        # Extract response and date, handling potential errors
        response_text = responses.get("response", "Error or invalid format.")
        date_text = responses.get('date', 'No date provided.')
        error_text = responses.get('error')

        if error_text:
            print(f"Error processing {image_file}: {error_text}")
            # Optionally save errors to Excel or a log file
            save_to_excel(f"Error: {error_text}", date_text)
        else:
            print(f"Immatriculation: {response_text}")
            save_to_excel(response_text, date_text)

        # Add delay between requests to avoid rate limiting or overwhelming the API
        time.sleep(10)

    print("Finished processing all images.")
