import base64
import json
import os
import traceback
import uuid

from flask import Flask, request, redirect
from flask_cors import CORS
from werkzeug.exceptions import HTTPException

import detector

app = Flask(__name__)
CORS(app)

APP_VERSION = "0.0.1"


@app.route('/api/v1/detect-gender-and-age', methods=['POST'])
def detect_gender_and_age():
    fid = str(uuid.uuid4())

    f = request.files['image']
    f_path = "uploads/" + fid + ".jpg"
    f.save(f_path)

    out = detector.get_gender_and_age(f_path)
    os.remove(f_path)

    result = {
        "app_version": APP_VERSION,
        "image": "data:image/jpg;base64," + base64.b64encode(out['image']).decode('ascii'),
        "results": out['results']
    }

    return json.dumps(result), 200


@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": traceback.format_exc()
    })
    return response


@app.route('/', methods=['POST', 'GET'])
def main_route():
    return redirect("static/detect.html", code=302)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5100)
