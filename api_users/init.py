from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from conf import DB_URI, KEY_VALUE


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["JSON_SORT_KEYS"] = False
db = SQLAlchemy(app)


cors = CORS(app, resources={r"/*": {"origins": "*"}})


# EXTRA 2
@app.before_request
def auth():
    headers = request.headers
    auth = headers.get("Api-Token")
    if auth != KEY_VALUE:
        return jsonify({"message": "ERROR: Resource Unauthorized!"}), 401