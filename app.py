import requests, os, uuid, json
from dotenv import load_dotenv
from flask import Flask, request, render_template

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        original_text = request.form['text']
        target_language = request.form['language']

        # Retrieve environment variables
        key = os.environ.get('KEY')
        endpoint = os.environ.get('ENDPOINT')
        location = os.environ.get('LOCATION')

        # Construct the URL for the translation API
        path = '/translate?api-version=3.0'
        target_language_parameter = '&to=' + target_language
        constructed_url = endpoint + path + target_language_parameter

        # Set up headers for the API request
        headers = {
            'Ocp-Apim-Subscription-Key': key,
            'Ocp-Apim-Subscription-Region': location,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

        # Prepare the request body
        body = [{'text': original_text}]

        try:
            # Make the API request
            translator_request = requests.post(constructed_url, headers=headers, json=body)
            translator_request.raise_for_status()  # Raise an error for bad status codes

            # Parse the response
            translator_response = translator_request.json()
            translated_text = translator_response[0]['translations'][0]['text']
        except requests.exceptions.RequestException as e:
            # Handle errors (e.g., network issues, invalid API key)
            return render_template('error.html', error_message=str(e))

        # Render the results page with the translated text
        return render_template('results.html', translated_text=translated_text, original_text=original_text, target_language=target_language)

    # Render the index page for GET requests
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)