import json
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    response = {"message": "Hello from Digital Ocean"}
    return json.dumps(response), 200, {"Content-Type": "application/json"}

if __name__ == '__main__':
    app.run(host='0.0.0.0')
