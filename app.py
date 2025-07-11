from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable cross-origin requests (important for frontend)

@app.route('/')
def home():
    return jsonify({"message": "Sale Tracker backend is running!"})

if __name__ == '__main__':
    app.run(debug=True)

    