# Image Upload and Generate Text Description of an image API

## Overview
This project provides two APIs using Python and Flask. The first API handles image uploads and uses the Hugging Face image-to-text pipeline to generate text descriptions of the images. The second API retrieves and displays all uploaded images along with their descriptions. Additionally, the application checks if an image has been uploaded previously to avoid redundant processing.

## Objectives
1. **API 1: Image Upload and Text Generation**
    - Allows users to upload an image.
    - Uses the Hugging Face image-to-text pipeline to generate a textual description of the uploaded image.
    - Stores the image path and the generated text description in a SQLite database.
    - Returns the text description as a response to the API call.
2. **API 2: Display Uploaded Images and Texts**
    - Retrieves and displays all images and their associated text descriptions from the SQLite database.
    - Provides a clear and structured response that includes both the image paths and their descriptions.
3. **Bonus Challenge: Efficient Text Retrieval for Repeated Images**
    - Checks if an image has already been uploaded based on its hash.
    - If the image is recognized as a duplicate, retrieves and returns the stored text description from the database instead of processing the image again.

## Technical Requirements
- Python 3.9.5 and Flask for the server setup.
- Hugging Face transformers library for the image-to-text pipeline.
- SQLite for data storage and management.
- Secure and efficient file uploads and data management.

## Setup and Running the Flask Application

### Prerequisites
- Python 3.9.5
- pip (Python package installer)

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/srishtipanwar/Image_API.git
    cd Image_API
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirement.txt
    ```

### Running the Application
1. Initialize the database:
    ```bash
    python main.py
    ```

2. The Flask application will start running at `http://127.0.0.1:5000`.

## API Endpoints

### 1. Upload Image and Generate Text Description
- **URL:** `/upload`
- **Method:** `POST`
- **Request:**
    - Form-data: `image` (file)
- **Response:**
    - `200 OK`: `{ "description": "Generated text description of the image" }`
    - `400 Bad Request`: `{ "error": "No image file provided" }`

### 2. Retrieve Uploaded Images and Texts
- **URL:** `/images`
- **Method:** `GET`
- **Response:**
    - `200 OK`: `[{ "path": "path/to/image.jpg", "description": "Generated text description of the image" }, ...]`

## Assumptions and Design Decisions
- The image hash is calculated using the MD5 algorithm to check for duplicates.
- The images are stored in the `uploads/` directory.
- The SQLite database is used for simplicity and ease of use.
- Error handling is implemented to provide clear messages for different failure scenarios.

## Dependencies
- Flask
- PIL (Pillow)
- transformers
- SQLite3

