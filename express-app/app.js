const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const app = express();
const PORT = 3000;

app.use(express.json());

const db = new sqlite3.Database('./blog.db', sqlite3.OPEN_READWRITE, (err) => {
  if (err) return console.error(err.message);
  console.log('Connected to the blog.db SQLite database.');
});

app.post('/users', (req, res) => {
  const { username, email, passwordHash } = req.body;
  db.run(`INSERT INTO Users (Username, Email, PasswordHash) VALUES (?, ?, ?)`, [username, email, passwordHash], function(err) {
    if (err) {
      return console.log(err.message);
    }
    res.send({ message: "User created successfully", userId: this.lastID });
  });
});

app.post('/posts', (req, res) => {
  const { userID, title, content } = req.body;
  db.run(`INSERT INTO Posts (UserID, Title, Content) VALUES (?, ?, ?)`, [userID, title, content], function(err) {
    if (err) {
      return console.log(err.message);
    }
    res.send({ message: "Post created successfully", postId: this.lastID });
  });
});

app.post('/comments', (req, res) => {
  const { postID, userID, comment } = req.body;
  db.run(`INSERT INTO Comments (PostID, UserID, Comment) VALUES (?, ?, ?)`, [postID, userID, comment], function(err) {
    if (err) {
      return console.log(err.message);
    }
    res.send({ message: "Comment added successfully", commentId: this.lastID });
  });
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});