from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

DATABASE = 'blog.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  
    return conn

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO Users (Username, Email, PasswordHash) VALUES (?, ?, ?)",
                   (data['username'], data['email'], data['passwordHash']))
    conn.commit()
    conn.close()
    
    return jsonify({"message": "User created successfully"}), 201

@app.route('/posts', methods=['POST'])
def create_post():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO Posts (UserID, Title, Content) VALUES (?, ?, ?)",
                   (data['userID'], data['title'], data['content']))
    conn.commit()
    conn.close()
    
    return jsonify({"message": "Post created successfully"}), 201

@app.route('/comments', methods=['POST'])
def create_comment():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO Comments (PostID, UserID, Comment) VALUES (?, ?, ?)",
                   (data['postID'], data['userID'], data['comment']))
    conn.commit()
    conn.close()
    
    return jsonify({"message": "Comment added successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)
