from flask import Flask,jsonify
import logging

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route('/status')
def get_status():
    logging.info('{{TIMESTAMP}}, {{ ENDPOINT_NAME}} endpoint was reached')
    return jsonify(result="OK - healthy")

@app.route('/metrics')
def get_metrics():
    logging.info('{{TIMESTAMP}}, {{ ENDPOINT_NAME}} endpoint was reached')
    return jsonify(data={'UserCount': 140, 'UserCountActive': 23})

if __name__ == "__main__":
    logging.basicConfig(filename='app.log',level=logging.DEBUG)
    app.run(host='0.0.0.0')
