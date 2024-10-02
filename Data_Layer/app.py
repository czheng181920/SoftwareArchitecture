from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/store', methods=['POST'])
def store_data():
    data = request.get_json()
    #use logic.py to store data in the database
    return f"Data stored", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
