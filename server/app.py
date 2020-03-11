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
    return jsonify(
        {
            '_id': 1,
            'title': "Test Card",
            'name': "Aiden Kennedy",
            'createDate':"10.10.10",
            'info':"This is a test of wether or not we can pull from an api",
            'uploadDate':"12-12-12"
        },
        {
            '_id': 2,
            'title': "Test Card 2 the electric boogaloo",
            'name': "Carlo Megehan",
            'createDate':"6.9.42",
            'info':"Test fo' 2 cards",
            'uploadDate':"3.15.14"
        }
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')