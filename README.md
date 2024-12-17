

# Parkinson's Disease Detection API

This Flask-based web application detects Parkinson's disease from an input image. It leverages a pre-trained Keras model for classification and provides results via a RESTful API and a user-friendly interface.


## Project Overview

The application accepts an image, processes it, and uses a deep learning model to classify whether the input corresponds to a person with Parkinson's disease or a healthy individual. The model achieves **93% accuracy** on the validation data.

---

## Features

- RESTful API endpoint for prediction.
- Image preprocessing for model compatibility.
- User-friendly interface for inputting and visualizing results.
- Lightweight Flask backend for deployment.

---

## Requirements

To run this project, ensure the following dependencies are installed:

- **Python** >= 3.7
- TensorFlow
- Flask
- Pillow
- NumPy

### Python Libraries
Install all the necessary libraries using pip:

```bash
pip install flask tensorflow pillow numpy
```

---

## Setup and Installation

Follow these steps to set up and run the project:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repository-link.git
   cd parkinsons-disease-detector
   ```

2. **Add the Model**:
   Place the pre-trained model file (`parkinson_disease_detection_model(93%).h5`) in the project directory.

3. **Install Dependencies**:
   Run the following command:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   Start the Flask development server:
   ```bash
   python app.py
   ```

5. **Access the App**:
   Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

---

## How to Use

1. **Upload Image**:
   Use the provided HTML interface (`prediction.html`) to upload an image.

2. **Submit**:
   The image is sent to the Flask backend for processing.

3. **Prediction**:
   The server returns the prediction:
   - `Parkinson`: Positive detection.
   - `Healthy`: No Parkinson's detected.

4. **API Call**:
   You can also make API calls programmatically.

---

## Folder Structure

```plaintext
project-root/
│
├── parkinson_disease_detection_model(93%).h5   # Pre-trained Keras model
├── app.py                                      # Flask server script
├── templates/
│   └── prediction.html                         # Frontend HTML file
└── README.md                                   # Documentation
```

---

## API Endpoints

### 1. **Home Page**
- **URL**: `/`
- **Method**: `GET`
- **Description**: Renders the HTML upload page.

### 2. **Prediction Endpoint**
- **URL**: `/predict`
- **Method**: `POST`
- **Request Body** (JSON):
   ```json
   {
       "image": "data:image/png;base64,<BASE64_ENCODED_IMAGE>"
   }
   ```
   - Ensure the image is base64-encoded.

- **Response** (JSON):
   ```json
   {
       "prediction": "Parkinson" or "Healthy"
   }
   ```

- **Error Response**:
   ```json
   {
       "error": "Error message"
   }
   ```

---


## Contact

For questions, contributions, or issues, please reach out to:

- **Samarth Otari**
- **Email**: otarisamarth49@gmail.com
- **GitHub**: https://github.com/samarth49

---

Happy Coding! 🚀
