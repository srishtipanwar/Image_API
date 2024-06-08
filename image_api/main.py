from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
import hashlib
from database import init_db, add_image_description, get_all_images, get_image_description
from transformers import pipeline
from PIL import Image

# Create a new Flask web application
app = Flask(__name__)

# Configure the folder to store uploaded images
app.config['UPLOAD_FOLDER'] = 'uploads/'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Initialize the Hugging Face image-to-text pipeline for image captioning
image_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-large")

@app.route('/upload', methods=['POST'])
def upload_image():
    # Check if an image file is part of the request
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    image = request.files['image']
    filename = secure_filename(image.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    # Calculate the MD5 hash of the image to detect duplicates
    image_hash = hashlib.md5(image.read()).hexdigest()
    image.seek(0)  # Reset file pointer to the beginning

    # Check if the image has already been uploaded
    existing_description = get_image_description(image_hash)
    if existing_description:
        return jsonify({'description': existing_description}), 200

    # Save the image to the upload folder
    image.save(file_path)

    # Open the saved image and generate a text description using the pipeline
    img = Image.open(file_path)
    description = image_to_text(img)[0]['generated_text']

    # Save the image hash, file path, and description to the database
    add_image_description(image_hash, file_path, description)

    return jsonify({'description': description}), 200

@app.route('/images', methods=['GET'])
def get_images():
    # Retrieve all images and their descriptions from the database
    images = get_all_images()
    return jsonify(images), 200

if __name__ == '__main__':
    # Initialize the database and start the Flask app
    init_db()
    app.run(host='127.0.0.1', port=5000, debug=True)

