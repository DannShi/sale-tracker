from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Basic root route (to confirm the app runs)
@app.route('/')
def home():
    return jsonify({"message": "Sale Tracker backend is running!"})

# Route to track a clothing item
@app.route('/track-item', methods=['POST'])
def track_item():
    data = request.get_json()

    # Check for required fields
    if 'name' not in data or 'url' not in data:
        return jsonify({"error": "Missing required fields: name and url"}), 400

    item = {
        'name': data['name'],
        'url': data['url'],
        'size': data.get('size'),
        'color': data.get('color')
    }

    return jsonify({"message": "Item tracked successfully", "item": item}), 201

# View tracked items (fake list for now)
@app.route('/tracked-items', methods=['GET'])
def get_items():
    return jsonify([{"name": "Sample item"}]), 200

if __name__ == '__main__':
    app.run(debug=True)
