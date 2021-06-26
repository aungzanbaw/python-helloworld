from flask import Flask, json
import logging, datetime


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Udacity!"


@app.route("/status")
def status():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )
    # log here
    app.logger.info("/status hit at {date}".format(date=datetime.datetime.now()))
    return response


@app.route("/metrics")
def metrics():
    response = app.response_class(
        response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
        status=200,
        mimetype="appliction/json"
    )
    app.logger.info("/metrics hit at {date}".format(date=datetime.datetime.now()))
    return response

if __name__ == "__main__":
    logging.basicConfig(filename='app.log', level=logging.DEBUG)
    app.run(host='0.0.0.0',use_reloader=True, use_debugger=True, use_evalex=True)