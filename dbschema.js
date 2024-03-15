const sqlite3 = require('sqlite3').verbose();
const db = new sqlite3.Database('./blog.db');

db.serialize(function() {
 
  db.run(`CREATE TABLE IF NOT EXISTS Users (
    UserID INTEGER PRIMARY KEY,
    Username TEXT NOT NULL,
    Email TEXT NOT NULL UNIQUE,
    PasswordHash TEXT NOT NULL
  );`);

  
  db.run(`CREATE TABLE IF NOT EXISTS Posts (
    PostID INTEGER PRIMARY KEY,
    UserID INTEGER NOT NULL,
    Title TEXT NOT NULL,
    Content TEXT NOT NULL,
    PublishDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(UserID) REFERENCES Users(UserID)
  );`);

  
  db.run(`CREATE TABLE IF NOT EXISTS Comments (
    CommentID INTEGER PRIMARY KEY,
    PostID INTEGER NOT NULL,
    UserID INTEGER NOT NULL,
    Comment TEXT NOT NULL,
    CommentDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(PostID) REFERENCES Posts(PostID),
    FOREIGN KEY(UserID) REFERENCES Users(UserID)
  );`);
});

db.close();
