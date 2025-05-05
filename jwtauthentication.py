from flask import Flask, request, jsonify
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required,
    get_jwt_identity, get_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta
import mysql.connector

app = Flask(__name__)


con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="user"
)


app.config['JWT_SECRET_KEY'] = 'b9e5f4c6a7d34856'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=5)
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access']
jwt = JWTManager(app)


blacklist = set()


@app.route("/register", methods=["POST"])
def register_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    hashed = generate_password_hash(password)
    cur = con.cursor()
    cur.execute("SELECT * FROM user_data WHERE email=%s", (email,))
    if cur.fetchone():
        return jsonify(f"User with {email} already exists!")
    cur.execute("INSERT INTO user_data (email, password) VALUES (%s, %s)", (email, hashed))
    con.commit()
    return jsonify("User registered successfully!")


@app.route("/login", methods=["POST"])
def user_login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    cur = con.cursor(dictionary=True)
    cur.execute("SELECT * FROM user_data WHERE email=%s", (email,))
    user = cur.fetchone()

    if user and check_password_hash(user['password'], password):
        access_token = create_access_token(identity=email)
        return jsonify(access_token=access_token)
    else:
        return jsonify("Invalid credentials!")

@app.route("/token_detail", methods=["GET"])
@jwt_required()
def get_details():
    return jsonify(get_jwt())

@app.route("/profile", methods=["GET"])
@jwt_required()
def user_profile():
    current_user = get_jwt_identity()
    return jsonify(f"Hello, {current_user} This is your profile.")


@app.route("/users", methods=["GET"])
@jwt_required()
def get_users():
    cur = con.cursor()
    cur.execute("SELECT id, email FROM user_data ORDER BY id ASC")
    result = cur.fetchall()
    return jsonify(result)

@app.route("/update/<int:id>", methods=["PUT"])
@jwt_required()
def update_user(id):
    data = request.get_json()
    new = data.get('email')
    cur = con.cursor()
    cur.execute("UPDATE user_data SET email = %s WHERE id = %s", (new, id))
    con.commit()
    return (f"Email id of user with id {id} is now {new} has been updated successfully!")

@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
    jti = jwt_payload['jti']
    return jti in blacklist


@app.route("/logout", methods=["POST"])
@jwt_required()
def user_logout():
    jti = get_jwt()['jti']
    blacklist.add(jti)
    return jsonify("User successfully logged out.")

if __name__ == '__main__':
    app.run(debug=True)
