from flask import Flask, request, jsonify
from app.tasks import add
import random


app = Flask(__name__)

@app.route('/')
def index():
    result = add.delay(10, 20)

    print("index")
    return "index"


@app.route('/add', methods=['POST'])
def add_numbers():
    data = request.json
    x = data.get('x', 0)
    y = data.get('y', 0)

    x = random.randint(1,10000000)
    y = random.randint(1,10000000)

    result = add.delay(x, y)

    return jsonify({'task_id': result.id, 'status': 'Processing...'}), 202

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)