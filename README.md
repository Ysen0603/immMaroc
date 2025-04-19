# Moroccan License Plate Extractor

## Description

This project uses the Google Gemini Vision API to extract license plate information (immatriculation numbers) from images of Moroccan license plates. It processes images found in the `cars/` directory and saves the extracted data along with the processing timestamp to an Excel file (`responses.xlsx`).

## Project Structure

```
.
├── .env                # Stores the GENAI_API_KEY (ignored by git)
├── .gitignore          # Specifies intentionally untracked files that Git should ignore
├── main.py             # Main entry point for the script
├── README.md           # This file
├── responses.xlsx      # Output Excel file with extracted data (ignored by git)
├── cars/               # Directory containing input images (ignored by git)
│   └── ... (image files)
└── src/                # Source code directory
    ├── __init__.py     # Makes src a Python package (optional)
    ├── gemini_handler.py # Handles interaction with the Gemini API
    ├── processing.py   # Contains the core image processing logic
    └── utils/          # Utility functions
        ├── __init__.py # Makes utils a Python package (optional)
        ├── excel_handler.py # Handles saving data to Excel
        └── validation.py  # Contains validation logic for immatriculation format
```

## Setup

1.  **Clone the repository (if applicable):**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    *Create a `requirements.txt` file with the necessary packages:*
    ```txt
    google-generativeai
    python-dotenv
    Pillow
    openpyxl
    ```
    *Then install them:*
    ```bash
    pip install -r requirements.txt
    ```

4.  **Create the `.env` file:**
    Create a file named `.env` in the root directory and add your Google Gemini API key:
    ```
    GENAI_API_KEY='YOUR_API_KEY_HERE'
    ```

5.  **Create the `cars/` directory:**
    Make sure the `cars/` directory exists in the root of the project and place the images you want to process inside it.

## Usage

Run the main script from the root directory:

```bash
python main.py
```

The script will:
- Read images from the `cars/` directory.
- Call the Gemini API to extract license plate numbers.
- Validate the format of the extracted numbers.
- Save the valid numbers and the processing date/time to `responses.xlsx`.
- Print progress and any errors to the console.
