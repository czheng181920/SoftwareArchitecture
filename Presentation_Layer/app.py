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
@app.route('/addMeeting', methods=['POST'])
def submit():
    data = request.get_json()
    print("Data sent to Business Layer")
    url = 'http://{BUSINESS_LAYER_IP}:5001/meeting'
    response = requests.post(url, json=data)
    
    return jsonify({"message": "Data sent to Business Layer", "response": response.text})


@app.route('/allMeeting', methods=['GET'])
def getMeetings():
    print("Get all meetings from Business Layer")
    url = 'http://{BUSINESS_LAYER_IP}:5001/meetings'
    response = request.get(url)
    return jsonify(response.json()), response.status_code


@app.route('/meetingByID', methods=['GET'])
def getMeetingByID():
    data = request.get_json()
    meeting_id = data.get('meeting-id')
    print("Meeting id to by found sent to Business Layer")
    url = 'http://{BUSINESS_LAYER_IP}:5001//meeting/{}'.format(meeting_id)
    response = requests.get(url)
    return jsonify(response.json()), response.status_code


@app.route('/updateMeeting', methods=['PUT'])
def updateMeetingByID():
    data = request.get_json()
    meeting_id = data.get('meeting_id')
    print("Meeting id to be updated sent to Business Layer")
    url = 'http://{BUSINESS_LAYER_IP}:5001//meeting/{}'.format(meeting_id) 
    response = requests.put(url, data)
    return jsonify(response.json()), response.status_code

@app.route('/deleteMeeting', methods=['DELETE'])
def deleteMeeting():
    data = request.get_json()
    meeting_id = data.get('meeting_id')
    print("Meeting id to be deleted sent to Business Layer")
    url = 'http://{BUSINESS_LAYER_IP}:5001//meeting/{}'.format(meeting_id) 
    response = requests.delete(url)
    return jsonify(response.json()), response.status_code

@app.route('/listofCalendars', methods=['GET'])
def getListCalendars():
    data = request.get_json()
    meeting_id = data.get('meeting_id')
    print("Meeting id of list of calendars sent to Business Layer")
    url = 'http://{BUSINESS_LAYER_IP}:5001//meeting/{}/calendars'.format(meeting_id) 
    response = requests.get(url)
    return jsonify(response.json()), response.status_code

@app.route('/listofParticipants', methods=['GET'])
def getListParticipants():
    data = request.get_json()
    meeting_id = data.get('meeting_id')
    print("Meeting id of list of participants sent to Business Layer")
    url = 'http://{BUSINESS_LAYER_IP}:5001//meeting/{}/participants'.format(meeting_id) 
    response = requests.get(url)
    return jsonify(response.json()), response.status_code

@app.route('/listofAttachments', methods=['GET'])
def getListAttachments():
    data = request.get_json()
    meeting_id = data.get('meeting_id')
    print("Meeting id of list of attachments sent to Business Layer")
    url = 'http://{BUSINESS_LAYER_IP}:5001//meeting/{}/attachments'.format(meeting_id) 
    response = requests.get(url)
    return jsonify(response.json()), response.status_code




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug = True)
