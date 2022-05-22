from flask import Flask, render_template, request
import requests, os, uuid, json
from do import do
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('trans.html')


@app.route('/res', methods=['GET'])
def result():
    return render_template('result.html')




@app.route('/', methods=['POST'])
def index_post():
    # Read the values from the form
    original_text = request.form['text']

    final = do(original_text)
    if (final=="難過"):
        final = "*****"

    target_language = request.form['language']
    # print(original_text)
    # print(target_language)

    # Load the values from .env
    
    # key = os.environ['KEY']
    # endpoint = os.environ['ENDPOINT']
    # location = os.environ['LOCATION']

    # Indicate that we want to translate and the API version (3.0) and the target language
    
    # path = '/translate?api-version=3.0'
    
    # Add the target language parameter

    # target_language_parameter = '&to=' + target_language
    # print(target_language_parameter)
    # Create the full URL

    # constructed_url = endpoint + path + target_language_parameter

    # Set up the header information, which includes our subscription key
    
    # headers = {
    #     'Ocp-Apim-Subscription-Key': key,
    #     'Ocp-Apim-Subscription-Region': location,
    #     'Content-type': 'application/json',
    #     'X-ClientTraceId': str(uuid.uuid4())
    # }

    # Create the body of the request with the text to be translated
    body = [{ 'text': original_text }]
    print(body)
    # Make the call using post
    # translator_request = requests.post(constructed_url, headers=headers, json=body)
    # Retrieve the JSON response
    # translator_response = translator_request.json()
    # Retrieve the translation
    # translated_text = translator_response[0]['translations'][0]['text']

    # Call render template, passing the translated text,
    # original text, and target language to the template
    return render_template(
        'trans.html',
        translated_text=final,
        original_text=original_text,
        target_language=target_language
    )

