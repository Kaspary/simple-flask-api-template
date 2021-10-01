from flask import jsonify
from core import app

@app.route('', methods=['GET'])
def core():
    return 'Flask Template - OK', 200
