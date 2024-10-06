from flask import Flask, render_template, render_template, jsonify, request
import requests
from dotenv import load_dotenv
import os

app = Flask(__name__)

#load enviornmental variables from .env file
load_dotenv()

# Get Business Layer IP
#TODO: need to change this in template.env
BUSINESS_LAYER_IP = os.getenv('BUSINESS_LAYER_IP') 

# serve the index.html file
@app.route('/')
def home():
    return render_template('index.html')

# Endpoint to handle requests from the HTML page
@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    print("Data sent to Business Layer")
    response = send_to_business_layer(data)
    
    return jsonify({"message": "Data sent to Business Layer", "response": response})

def send_to_business_layer(data):
    #TODO: this should theoretically work but still needs to be tested and debugged between two machines 
    url = 'http://{BUSINESS_LAYER_IP}:5001/process'
    response = requests.post(url, json=data)
    return response.text




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug = True)
