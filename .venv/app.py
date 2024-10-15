from flask import Flask, request, jsonify, render_template  # Import render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np
import base64
from PIL import Image
import io


app = Flask(__name__)

# Load the pre-trained model
model = load_model('parkinson_disease_detection_model(93%).h5')

def preprocess_image(image, target_size):
    if image.mode != 'RGB':
        image = image.convert('RGB')
    image = image.resize(target_size)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = image / 255.0
    return image

# Route to render the HTML file
@app.route('/')
def index():
    return render_template('prediction.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        image_data = data['image'].split(',')[1]  # Remove header part
        decoded_image = base64.b64decode(image_data)
        image = Image.open(io.BytesIO(decoded_image))

        # Preprocess the image
        processed_image = preprocess_image(image, target_size=(128, 128))

        # Make prediction
        prediction = model.predict(processed_image)
        
        # Determine the result
        if prediction[0][0] > 0.5:
            result = 'Parkinson'
        else:
            result = 'Healthy'
        
        return jsonify({'prediction': result})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)