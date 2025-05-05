from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
  {"id": 1, "username": "john doe", "email": "johndoe@example.com", "password": "1234"},
  {"id": 2, "username": "jane smith", "email": "janesmith@example.com", "password": "5678"},
  {"id": 3, "username": "alice brown", "email": "alicebrown@example.com", "password": "abcd"},
  {"id": 4, "username": "bob jones", "email": "bobjones@example.com", "password": "efgh"},
  {"id": 5, "username": "charlie black", "email": "charlieblack@example.com", "password": "ijkl"},
  {"id": 6, "username": "david white", "email": "davidwhite@example.com", "password": "mnop"},
  {"id": 7, "username": "emily clark", "email": "emilyclark@example.com", "password": "qrst"},
  {"id": 8, "username": "frank hall", "email": "frankhall@example.com", "password": "uvwx"},
  {"id": 9, "username": "grace adams", "email": "graceadams@example.com", "password": "yz12"},
  {"id": 10, "username": "henry young", "email": "henryyoung@example.com", "password": "3456"},
  {"id": 11, "username": "irene king", "email": "ireneking@example.com", "password": "7890"},
  {"id": 12, "username": "jack lee", "email": "jacklee@example.com", "password": "abcd"},
  {"id": 13, "username": "karen bell", "email": "karenbell@example.com", "password": "efgh"},
  {"id": 14, "username": "leo turner", "email": "leoturner@example.com", "password": "ijkl"},
  {"id": 15, "username": "mia walker", "email": "miawalker@example.com", "password": "mnop"},
  {"id": 16, "username": "nathan scott", "email": "nathanscott@example.com", "password": "qrst"},
  {"id": 17, "username": "olivia cooper", "email": "oliviacooper@example.com", "password": "uvwx"},
  {"id": 18, "username": "paul morris", "email": "paulmorris@example.com", "password": "yz12"},
  {"id": 19, "username": "quinn reed", "email": "quinnreed@example.com", "password": "3456"},
  {"id": 20, "username": "rachel baker", "email": "rachelbaker@example.com", "password": "7890"},
  {"id": 21, "username": "steve hill", "email": "stevehill@example.com", "password": "abcd"},
  {"id": 22, "username": "tina ward", "email": "tinaward@example.com", "password": "efgh"},
  {"id": 23, "username": "uma diaz", "email": "umadiaz@example.com", "password": "ijkl"},
  {"id": 24, "username": "victor long", "email": "victorlong@example.com", "password": "mnop"},
  {"id": 25, "username": "wendy rice", "email": "wendyrice@example.com", "password": "qrst"},
  {"id": 26, "username": "xander fox", "email": "xanderfox@example.com", "password": "uvwx"},
  {"id": 27, "username": "yara grant", "email": "yaragrant@example.com", "password": "yz12"},
  {"id": 28, "username": "zack hughes", "email": "zackhughes@example.com", "password": "3456"},
  {"id": 29, "username": "abby frank", "email": "abbyfrank@example.com", "password": "7890"},
  {"id": 30, "username": "brian nash", "email": "briannash@example.com", "password": "abcd"},
  {"id": 31, "username": "cindy ortiz", "email": "cindyortiz@example.com", "password": "efgh"},
  {"id": 32, "username": "derek stone", "email": "derekstone@example.com", "password": "ijkl"},
  {"id": 33, "username": "ella watts", "email": "ellawatts@example.com", "password": "mnop"},
  {"id": 34, "username": "fred bond", "email": "fredbond@example.com", "password": "qrst"},
  {"id": 35, "username": "gina greene", "email": "ginagreene@example.com", "password": "uvwx"},
  {"id": 36, "username": "harry klein", "email": "harryklein@example.com", "password": "yz12"},
  {"id": 37, "username": "iris sharp", "email": "irissharp@example.com", "password": "3456"},
  {"id": 38, "username": "james price", "email": "jamesprice@example.com", "password": "7890"},
  {"id": 39, "username": "kyle snow", "email": "kylesnow@example.com", "password": "abcd"},
  {"id": 40, "username": "lisa carter", "email": "lisacarter@example.com", "password": "efgh"},
  {"id": 41, "username": "matt woods", "email": "mattwoods@example.com", "password": "ijkl"},
  {"id": 42, "username": "nina ford", "email": "ninaford@example.com", "password": "mnop"},
  {"id": 43, "username": "owen dean", "email": "owendean@example.com", "password": "qrst"},
  {"id": 44, "username": "pam wells", "email": "pamwells@example.com", "password": "uvwx"},
  {"id": 45, "username": "ron york", "email": "ronyork@example.com", "password": "yz12"},
  {"id": 46, "username": "sara zane", "email": "sarazane@example.com", "password": "3456"},
  {"id": 47, "username": "tom casey", "email": "tomcasey@example.com", "password": "7890"},
  {"id": 48, "username": "ursula levy", "email": "ursulalevy@example.com", "password": "abcd"},
  {"id": 49, "username": "vince ray", "email": "vinceray@example.com", "password": "efgh"},
  {"id": 50, "username": "wanda lane", "email": "wandalane@example.com", "password": "ijkl"}
]


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Home API!"})



@app.route("/greet/<username>", methods=["GET"])
def greet(username):
    return jsonify({"message": f"Hello {username.capitalize()}!"})



@app.route("/about", methods=["GET"])
def about():
    return jsonify({"info": "This is the about page."})

@app.route("/contact", methods=["GET"])
def contact():
    return jsonify({"contact": "You can contact us at contact@example.com"})

@app.route("/product", methods=["GET"])
def product():
    return jsonify({"product": "Product details go here."})

@app.route("/review", methods=["GET"])
def review():
    return jsonify({"reviews": ["Great product!", "Would buy again!"]})





@app.route("/login", methods=["GET"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    for user in users:  
        if user["username"] == username and user["password"] == password:
            return jsonify({"message": "Login successful!", "user": user}), 200

    return jsonify({"error": "Invalid credentials"}), 401





@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password:
        return jsonify({"error": "Missing required fields"}), 400

 
    return jsonify({"message": f"User {username} registered successfully!"}), 201

@app.route("/echo", methods=['POST'])
def echo():
    try:
        data = request.get_json(force=True)
        print("Received data:", data)
        return jsonify({'you_sent': data})
    except Exception as e:
        print("Error:", e)
        return jsonify({'error': str(e)})




if __name__ == "__main__":
    app.run(debug=True)
