from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable cross-origin requests (important for frontend)

@app.route('/')
def home():
    return jsonify({"message": "Sale Tracker backend is running!"})

if __name__ == '__main__':
    app.run(debug=True)

# In-memory store for now
tracked_items = []

@app.route('/track-item', methods=['POST'])
def track_item():
    data = request.get_json()

    required_fields = ['name', 'url']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Missing required field: {field}'}), 400

    item = {
        'name': data['name'],
        'url': data['url'],
        'size': data.get('size'),
        'color': data.get('color')
    }

    tracked_items.append(item)
    return jsonify({'message': 'Item tracked successfully', 'item': item}), 201

@app.route('/tracked-items', methods=['GET'])
def get_tracked_items():
    return jsonify(tracked_items), 200

    