# Email/SMS Spam Classifier

This project is a web application for classifying messages as spam or not spam using machine learning. The application uses Streamlit for the web interface, NLTK for text preprocessing, and a pre-trained machine learning model for classification.
You can acces the app here https://email-sms-spam-classifier2318.streamlit.app/

## Features

- **Text Input:** Users can input an email or SMS message.
- **Spam Prediction:** The application processes the input message and predicts whether it is spam or not.
- **Text Preprocessing:** The text is preprocessed using tokenization, stopword removal, and stemming.

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Step-by-Step Guide

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/spam-classifier.git
    cd spam-classifier
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Download necessary NLTK data:

    ```python
    import nltk
    nltk.download('stopwords')
    nltk.download('punkt')
    ```

4. Ensure you have the following files in the project directory:
    - `vectorizer.pkl` (the vectorizer)
    - `model.pkl` (the pre-trained model)

## Usage

First run the python notebook and generate model.pkl and vectorizer.pkl and save them in the directory where others files are also saved.

Now, To run the application, execute the following command in the project directory:

```bash
streamlit run app.py
```

Now, enter the msg you want to know whether it is spam or not in the text area and click predict button. You will come to know whether the message entered is spam or not.
