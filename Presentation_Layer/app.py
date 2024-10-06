from flask import Flask, render_template, jsonify, request
import requests
from dotenv import load_dotenv
import os

app = Flask(__name__)

#load enviornmental variables from .env file
load_dotenv()

# Get Business Layer IP
#TODO: need to change this in template.env
# BUSINESS_LAYER_IP = os.getenv('BUSINESS_LAYER_IP') 
BUSINESS_LAYER_IP = '172.20.55.130' # neha ip

# serve the index.html file
@app.route('/')
def home():
    return render_template('index.html')

# Endpoint to handle requests from the HTML page
@app.route('/addMeeting', methods=['POST'])
def submit():
    data = request.get_json()
    print("Data sent to Business Layer")
    url = f'http://{BUSINESS_LAYER_IP}:5001/meeting'
    response = requests.post(url, json=data)
    
    return jsonify({"message": "Data sent to Business Layer", "response": response.text})


@app.route('/allMeetings', methods=['GET'])
def getMeetings():
    print("Get all meetings from Business Layer")
    url = f'http://{BUSINESS_LAYER_IP}:5001/meetings'
    response = requests.get(url)
    return jsonify(response.json()), response.status_code


@app.route('/meetingByID', methods=['GET'])
def getMeetingByID():
    data = request.get_json()
    meeting_id = data.get('meeting-id')
    print("Meeting id to by found sent to Business Layer")
    url = f'http://{BUSINESS_LAYER_IP}:5001/meeting/{meeting_id}'
    response = requests.get(url)
    return jsonify(response.json()), response.status_code


@app.route('/updateMeeting', methods=['PUT'])
def updateMeetingByID():
    data = request.get_json()
    title = data.get('title')
    date_time = data.get('date_time')
    location = data.get('location')
    details = data.get('details')
    
    meeting_id = data.get('meeting_id')
    print("Meeting id to be updated sent to Business Layer")
    url = f'http://{BUSINESS_LAYER_IP}:5001/meeting/{meeting_id}'
    response = requests.put(url, json={
        "title": title,
        "date_time": date_time,
        "location": location,
        "details": details
    })
    return jsonify(response.json()), response.status_code

@app.route('/deleteMeeting', methods=['DELETE'])
def deleteMeeting():
    data = request.get_json()
    meeting_id = data.get('meeting_id')
    print("Meeting id to be deleted sent to Business Layer")
    url = f'http://{BUSINESS_LAYER_IP}:5001/meeting/{meeting_id}'
    response = requests.delete(url)
    return jsonify(response.json()), response.status_code

@app.route('/listofCalendars', methods=['GET'])
def getListCalendars():
    data = request.get_json()
    meeting_id = data.get('meeting_id')
    print("Meeting id of list of calendars sent to Business Layer")
    url = f'http://{BUSINESS_LAYER_IP}:5001/meeting/{meeting_id}/calendars'
    response = requests.get(url)
    return jsonify(response.json()), response.status_code

@app.route('/listofParticipants', methods=['GET'])
def getListParticipants():
    data = request.get_json()
    meeting_id = data.get('meeting_id')
    print("Meeting id of list of participants sent to Business Layer")
    url = f'http://{BUSINESS_LAYER_IP}:5001/meeting/{meeting_id}/participants'
    response = requests.get(url)
    return jsonify(response.json()), response.status_code

@app.route('/listofAttachments', methods=['GET'])
def getListAttachments():
    data = request.get_json()
    meeting_id = data.get('meeting_id')
    print("Meeting id of list of attachments sent to Business Layer")
    url = f'http://{BUSINESS_LAYER_IP}:5001/meeting/{meeting_id}/attachments'
    response = requests.get(url)
    return jsonify(response.json()), response.status_code

@app.route('/addCalendar', methods=['POST'])
def addCalendar():
    data = request.get_json()
    url = f'http://{BUSINESS_LAYER_IP}:5001/calendar' 
    response = requests.post(url, data)
    return jsonify({"message": "Data sent to Business Layer", "response": response.text})

@app.route('/allCalendar', methods=['GET'])
def getCalendar():
    url = f'http://{BUSINESS_LAYER_IP}:5001/calendar' 
    response = requests.get(url)
    return jsonify(response.json()), response.status_code

@app.route('/findCalendarById', methods=['GET'])
def findCalendar():
    data = request.get_json()
    calendar_id = data.get('calendar_id')
    url = f'http://{BUSINESS_LAYER_IP}:5001/calendar/{calendar_id}'
    response = requests.get(url)
    return jsonify(response.json()), response.status_code

@app.route('/updateCalendar', methods=['PUT'])
def updateCalendar():
    data = request.get_json()
    calendar_id = data.get('calendar_id')
    url = f'http://{BUSINESS_LAYER_IP}:5001/calendar/{calendar_id}'
    response = requests.put(url, data)
    return jsonify(response.json()), response.status_code

@app.route('/deleteCalendar', methods=['DELETE'])
def deleteCalendar():
    data = request.get_json()
    calendar_id = data.get('calendar_id')
    url = f'http://{BUSINESS_LAYER_IP}:5001/calendar/{calendar_id}'
    response = requests.delete(url)
    return jsonify(response.json()), response.status_code

#/calendar/<calendar_id>/meetings
@app.route('/allMeetinginCalendar', methods=['GET'])
def meetingsInCalendar():
    data = request.get_json()
    calendar_id = data.get('calendar_id')
    url = f'http://{BUSINESS_LAYER_IP}:5001/calendar/{calendar_id}/meetings'
    response = requests.get(url, data)
    return jsonify(response.json()), response.status_code

@app.route('/addParticipant', methods=['POST'])
def addParticipant():
    data = request.get_json()
    url = f'http://{BUSINESS_LAYER_IP}:5001/participant'
    response = requests.post(url, data)
    return jsonify({"message": "Data sent to Business Layer", "response": response.text})

@app.route('/allParticipants', methods=['GET'])
def allParticipants():
    data = request.get_json()
    url = f'http://{BUSINESS_LAYER_IP}:5001/participants'
    response = requests.get(url)
    return jsonify(response.json()), response.status_code

@app.route('/participantsByID', methods=['GET'])
def participantById():
    data = request.get_json()
    participant_id = data.get('participant_id')
    url = f'http://{BUSINESS_LAYER_IP}:5001/participant/{participant_id}'
    response = requests.get(url)
    return jsonify(response.json()), response.status_code

@app.route('/updateParticipants', methods=['PUT'])
def updateParticipants():
    data = request.get_json()
    participant_id = data.get('participant_id')
    url = f'http://{BUSINESS_LAYER_IP}:5001/participant/{participant_id}'
    response = requests.put(url,data)
    return jsonify(response.json()), response.status_code

@app.route('/deleteParticipants', methods=['DELETE'])
def deleteParticipants():
    data = request.get_json()
    participant_id = data.get('participant_id')
    url = f'http://{BUSINESS_LAYER_IP}:5001/participant/{participant_id}'
    response = requests.delete(url)
    return jsonify(response.json()), response.status_code

@app.route('/addAttachment', methods=['POST'])
def addAttachment():
    data = request.get_json()
    url = f'http://{BUSINESS_LAYER_IP}:5001/attachment'
    response = requests.post(url, data)
    return jsonify({"message": "Data sent to Business Layer", "response": response.text})

@app.route('/allAttachment', methods=['GET'])
def allAttachments():
    data = request.get_json()
    url = f'http://{BUSINESS_LAYER_IP}:5001/attachment'
    response = requests.get(url)
    return jsonify(response.json()), response.status_code

@app.route('/attachmentById', methods=['GET'])
def attachmentsById():
    data = request.get_json()
    attachment_id = data.get('attachment_id')
    url = f'http://{BUSINESS_LAYER_IP}:5001/attachment/{attachment_id}'
    response = requests.get(url)
    return jsonify(response.json()), response.status_code

@app.route('/updateAttachment', methods=['PUT'])
def updateAttachment():
    data = request.get_json()
    attachment_id = data.get('attachment_id')
    url = f'http://{BUSINESS_LAYER_IP}:5001/attachment/{attachment_id}'
    response = requests.put(url,data)
    return jsonify(response.json()), response.status_code

@app.route('/deleteAttachment', methods=['DELETE'])
def deleteAttachment():
    data = request.get_json()
    attachment_id = data.get('attachment_id')
    url = f'http://{BUSINESS_LAYER_IP}:5001/attachment/{attachment_id}'
    response = requests.delete(url)
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug = True)
