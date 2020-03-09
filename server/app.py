from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # avoid Cross-Origin Resource Sharing (CORS) errors

# Declare routes by following the examples below
@app.route('/')
def index():
    return "Hello, World!" # return this data to the client

@app.route('/api/v1.0/card', methods=['GET'])
def get_tasks():
    return jsonify({'title': "Test Card",'name': "Aiden Kennedy",'createdDate':"10.10.10",'info':"This is a test of wether or not we can pull from an api",'uploadDate':"12-12-12"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')