from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="db",
            user="flaskuser",
            password="flaskpassword",
            database="flaskdb"
        )
        if connection.is_connected():
            print("Connection to MariaDB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

@app.route('/users', methods=['GET', 'POST'])
def manage_users():
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)

    if request.method == 'POST':
        new_user = request.json
        sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
        cursor.execute(sql, (new_user['name'], new_user['email']))
        connection.commit()
        return jsonify(new_user), 201

    elif request.method == 'GET':
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        return jsonify(users), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')
