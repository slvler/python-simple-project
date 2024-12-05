from flask import Flask, request, jsonify
import redis

app = Flask(__name__)

redis_client = redis.Redis(host='redis', port=6379)


@app.route('/', methods=['GET'])
def index():
    print("index")
    return "index"


@app.route('/set', methods=['POST'])
def set_value():
    key = request.form.get('key')
    value = request.form.get('value')
    redis_client.set(key, value)
    return jsonify({"message": f"Key '{key}' set with value '{value}'"}), 201


@app.route('/get/<key>', methods=['GET'])
def get_value(key):
    value = redis_client.get(key)
    if value:
        return jsonify({"message": f"Key '{key}' set with value '{value}'"}), 200
    return jsonify({"error": "Key not found"}), 404

@app.route('/delete/<key>', methods=['DELETE'])
def delete_value(key):
    result = redis_client.delete(key)
    if result:
        return jsonify({"message": f"Key '{key}' deleted"}), 200
    return jsonify({"error": "Key not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)