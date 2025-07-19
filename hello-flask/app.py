import os
from flask import Flask, jsonify
import MySQLdb

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask + MySQL app is running!"

@app.route('/users')
def get_users():
    db = MySQLdb.connect(
        host=os.environ.get("MYSQL_HOST"),
        user=os.environ.get("MYSQL_USER"),
        passwd=os.environ.get("MYSQL_PASSWORD"),
        db=os.environ.get("MYSQL_DATABASE")
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    db.close()
    return jsonify(users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
