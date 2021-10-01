import json
from flask import jsonify, render_template
from documentation import app

@app.route('', methods=['GET'])
def get_html_documentation():
    return render_template('index.html')


@app.route('/postman', methods=['GET'])
def get_postman_documentation():
    try:
        with open('documentation/postman_collection.json', 'r') as file_obj:
            return jsonify(json.load(file_obj)), 200
    except FileNotFoundError as e:
        print('ERROR: ', str(e))
    return "", 404
