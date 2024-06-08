from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # CORS設定を追加

t = 0

@app.route('/')
def hello():
    return "Hello from Flask!"

@app.route('/message', methods=['POST'])
def process_message():
    t = t + 1
    return jsonify({'message': t})

if __name__ == '__main__':
    app.run(debug=True)