from flask import jsonify
from core import app

@app.route('', methods=['GET'])
def core():
    return jsonify({}), 200
