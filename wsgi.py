import json
from flask import Flask, Response, jsonify, request
from prediction import predict

application = Flask(__name__)


@application.route('/')
@application.route('/status')
def status():
    return jsonify({'status': 'ok'})


@application.route('/openapi')
def get_open_api_spec():
    with open('openapi.json', 'r') as file:
        spec = file.read()

    response = Response(
        response=spec,
        mimetype='application/json'
    )
    return response


@application.route('/predictions', methods=['POST'])
def create_prediction():
    data = request.data or '{}'
    body = json.loads(data)
    return jsonify(predict(body))
