# from flask import Flask, request, jsonify, send_file, Response
# import mysql.connector
# from werkzeug.security import generate_password_hash, check_password_hash

# app = Flask(__name__)

# con = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="file",  
#     auth_plugin='mysql_native_password'  
# )


#---------------DATABASE AND API -----------------------------------------


# @app.route("/data", methods=["GET"])
# def get_user():
#     cur = con.cursor(dictionary=True)
#     cur.execute("SELECT * FROM users_data")
#     result = cur.fetchall()
#     return jsonify(result)

# @app.route("/update", methods=["POST"])
# def add_user():
#     data = request.get_json()

#     name = data.get('name')
#     email = data.get('email')
#     phone = data.get('phone')
#     role = data.get('role')
#     password = data.get('password')

#     cur = con.cursor(dictionary=True)
#     sql = "INSERT INTO users_data (name, email, phone, role, password) VALUES (%s, %s, %s, %s, %s)"
#     val = (name, email, phone, role, password)
#     cur.execute(sql, val)
#     con.commit()

#     return jsonify(f"Data stored: {name} {email} {phone} {role} {password}")

# @app.route("/user/<int:id>", methods=['GET'])
# def user_id(id):

#     cur = con.cursor(dictionary=True)
#     sql = "SELECT * FROM users_data where id = %s"
#     val = (id,)
#     cur.execute(sql,val)
#     result = cur.fetchall()
#     if result:
#         return jsonify(result)
#     else:
#         return jsonify("No user found")
    
# @app.route("/user/<int:id>", methods=['PUT'])
# def update_user(id):
#     data = request.get_json()
#     cur = con.cursor(dictionary=True)
#     name = data.get('name')
#     email = data.get('email')
#     phone = data.get("phone")
#     role = data.get("role")
#     password = data.get("password")

#     sql = "UPDATE users_data SET name=%s, email=%s, phone=%s, role=%s, password=%s WHERE id=%s"
#     val = (name, email, phone, role, password, id)
#     cur.execute(sql,val)
#     con.commit()
#     if cur.rowcount == 0:
#         return jsonify("No user found")
#     return jsonify(f"Data of user with id {id} updated successfully!")

# @app.route("/delete/<int:id>", methods=["DELETE"])
# def delete_user(id):
#     cur = con.cursor(dictionary=True)
#     sql = "DELETE FROM users_data WHERE id=%s"
#     val = (id,)
#     cur.execute(sql,val)
#     con.commit()
#     if cur.rowcount == 0:
#         return jsonify("No user found")
#     return jsonify(f"User with id {id} deleted from database!")

# @app.route("/find", methods=["POST"])
# def find_data():
#     data = request.get_json()
#     cur = con.cursor(dictionary=True)
#     email = data.get('email')
#     password = data.get('password')
#     sql = "SELECT * FROM users_data WHERE email=%s or password=%s"
#     val = (email, password)
#     cur.execute(sql, val)
#     user = cur.fetchone()
#     print(user)
#     if user:
#         return jsonify(f"User with email: {email} and password: {password} exists")
#     else:
#         return jsonify("No user exists!")

# @app.route("/fetch", methods=["GET"])
# def fetch_data():
#     cur = con.cursor(dictionary=True)
#     page = int(request.args.get('page', 1))
#     limit = int(request.args.get('limit', 5))
#     offset = (page-1)*limit
#     sql = "SELECT * FROM users_data LIMIT %s OFFSET %s"
#     val = (limit, offset)
#     cur.execute(sql, val)
#     result = cur.fetchall()
#     return jsonify(result)

# @app.route("/register", methods=["POST"])
# def register_user():
#     data = request.get_json()
#     name = data.get('name')
#     email = data.get('email')
#     phone = data.get("phone")
#     role = data.get("role")
#     password = data.get("password")
#     hashed = generate_password_hash(password)
#     cur = con.cursor(dictionary=True)
#     sql = "INSERT INTO users_data (name, email, phone, role, password) VALUES (%s, %s, %s, %s, %s)"
#     val = (name, email, phone, role, hashed)
#     cur.execute(sql,val)
#     con.commit()
#     return jsonify("User registered successfully!")


# if __name__ == '__main__':
#     app.run(debug=True)
