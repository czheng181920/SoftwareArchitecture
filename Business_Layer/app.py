from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    # result = send_to_data_layer(data)
    return f"Processed data: {data}", 200

def send_to_data_layer(data):
    url = 'http://<Data_Layer_IP>:5002/store'
    response = requests.post(url, json=data)
    return response.text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)