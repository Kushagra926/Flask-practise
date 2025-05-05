# from flask import Flask, request, jsonify, send_file, Response
# import mysql.connector
# import io
# import blob
# from werkzeug.security import generate_password_hash, check_password_hash

# app = Flask(__name__)

# con = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Kushagra@1234",
#     database="users",    #user, image, file 3 databases
#     auth_plugin='mysql_native_password'  
# @app.route("/upload", methods=["POST"])
# def upload_file():
#     file = request.files['file']
#     filename = file.filename
#     filetype = file.content_type
#     data = file.read()

#     sql = "INSERT INTO image_data (filename, filetype, data) VALUES (%s, %s, %s)"
#     val = (filename, filetype, data)
#     cur = con.cursor(dictionary=True)
#     cur.execute(sql, val)
#     con.commit()
#     return jsonify(f"File {filename} uploaded successfully to database.") 

# @app.route("/file/<int:id>", methods=["GET"])
# def fetch_data(id):
#     cur = con.cursor()
#     sql = "SELECT filename, filetype, data FROM image_data WHERE id=%s"
#     val = (id,)
#     cur.execute(sql,val)
#     result = cur.fetchone()
#     if result:
#         filename, filetype, data = result
#         return send_file(
#             io.BytesIO(data),
#             mimetype = filetype,
#             download_name = filename,
#             as_attachment=True
#         )
#     else:
#         return jsonify(f"File with id {id} not found!")
    
# @app.route("/fetch", methods=["GET"])
# def get_allfile():
#     cur = con.cursor(dictionary=True)
#     cur.execute("SELECT id, filename, filetype FROM image_data")
#     result = cur.fetchall()
#     if result:
#         return jsonify(result)
#     else:
#         return jsonify("No data found!")
    
# @app.route("/delete/<int:id>", methods=["DELETE"])
# def delete_data(id):
#     cur = con.cursor()
#     sql = "DELETE FROM image_data WHERE id=%s"
#     val = (id,)
#     cur.execute(sql,val)
#     con.commit()
#     if cur.rowcount == 0:
#         return jsonify("No data found")
#     else:
#         return jsonify(f"Data with id {id} deleted")

# if __name__ == '__main__':
#     app.run(debug=True)
