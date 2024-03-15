import sqlite3

connection = sqlite3.connect('blog.db')

with connection:
    cursor = connection.cursor()
    
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS Users (
        UserID INTEGER PRIMARY KEY,
        Username TEXT NOT NULL,
        Email TEXT NOT NULL UNIQUE,
        PasswordHash TEXT NOT NULL
    );""")
    
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS Posts (
        PostID INTEGER PRIMARY KEY,
        UserID INTEGER NOT NULL,
        Title TEXT NOT NULL,
        Content TEXT NOT NULL,
        PublishDate DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(UserID) REFERENCES Users(UserID)
    );""")
    
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS Comments (
        CommentID INTEGER PRIMARY KEY,
        PostID INTEGER NOT NULL,
        UserID INTEGER NOT NULL,
        Comment TEXT NOT NULL,
        CommentDate DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(PostID) REFERENCES Posts(PostID),
        FOREIGN KEY(UserID) REFERENCES Users(UserID)
    );""")

connection.close()
