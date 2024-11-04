from flask import Flask, jsonify, request
from sentiment import analyze_sentiment
from bias import analyze_bias
from consts import Endpoints

app = Flask(__name__)

@app.route('/sentiment', methods = ['GET'])
def sentiment():
    title = request.args.get(Endpoints.API)

    if not title:
        return jsonify({'error': 'title is required'}), 400

    res = analyze_sentiment(title)
    return jsonify(res)

@app.route("/bias", methods = ['GET'])
def bias():
    title = request.args.get(Endpoints.API)
    
    if not title:
        return jsonify({'error': 'title is required'}), 400
    
    res = analyze_bias(title)
    return jsonify(res)