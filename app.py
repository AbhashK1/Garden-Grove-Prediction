from flask import Flask, request, jsonify
from flask_cors import CORS
import model

app = Flask(__name__)
CORS(app)


@app.route('/predict', methods=['GET'])
def predictPrice():
    res = model.predict(request.args.get('name'))
    return jsonify(res)


@app.route('/getprice', methods=['GET'])
def predict():
    res = model.getPrice(request.args.get('name'))
    return jsonify(res)


if __name__ == '__main__':
    app.run(host="127.0.0.9", port=8080, debug=True)
