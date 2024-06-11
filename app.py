from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # CORS設定を追加

t = 0  # グローバル変数として定義

@app.route('/')
def hello():
    return "Hello from Flask!"

@app.route('/message', methods=['POST'])
def process_message():
    global t  # グローバル変数を使用
    t += 1

    # 例: 外部APIにリクエストを送信
    response = requests.get('https://api.example.com/data')
    external_data = response.json()

    return jsonify({'message': t, 'external_data': external_data})

if __name__ == '__main__':
    app.run(debug=True)
