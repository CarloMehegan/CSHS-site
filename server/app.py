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

#heres that stuff that wont work
# @app.route('/api/v1.0/uploadpost', methods=['GET, POST'])
# def api_post():
#     conn = sqlite3.connect('posts.db')
#     cur = conn.cursor()
#     sqlthing = '''INSERT INTO Posts (name, title, createDate, uploadDate, info) VALUES (?,?,?,?,?)'''
#     val = ('John', 'Highway 21', '1-2-3', '5-30-20', 'bruh moment pog')
#     cur.execute(sqlthing, val)
#     # conn.commit()

#     return cur.lastrowid
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
