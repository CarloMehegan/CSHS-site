from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app) # avoid Cross-Origin Resource Sharing (CORS) errors

# Declare routes by following the examples below
@app.route('/')
def index():
    return "Hello, World!" # return this data to the client


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
    
@app.route('/api/v1.0/posts', methods=['GET'])
def api_all():
    conn = sqlite3.connect('posts.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_posts = cur.execute('SELECT * FROM Posts;').fetchall()

    return jsonify(all_posts)

def upload_post(values):
    conn = sqlite3.connect('posts.db')

    print ("Opened database successfully")

    command = "INSERT INTO Posts (name, title, createDate, uploadDate, info) VALUES (?,?,?,?,?)"
    conn.execute(command, values )

    conn.commit()

    print("Records created successfully with title: " + values[0])
    conn.close()
    

@app.route('/postmethod', methods=['GET','POST'])
def create_post():
    data = request.get_json() or {}
    # print(data['post_data'])
    upload_post(data['post_data'])
    return 'yes sirr'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
