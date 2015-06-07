from flask import Flask, Response, request, abort
from ciscophidget import Module1011

app = Flask(__name__)
phidget1011 = Module1011("10.10.10.250", "0022bdcf4574")

@app.route('/api/v1/analog/<int:port>', methods=["GET"])
def api_analog(port):
    """
    Function to handle HTTP GET Request for reading analog ports values.
    """
    try:
        value = str(phidget1011.get_analog_value(port))
        return Response(value, mimetype="application/json")
    except:
        abort(404)

@app.route('/api/v1/digital/<int:port>', methods=["GET", "POST"])
def api_digital(port):
    """
    Function to handle HTTP GET/POST Request for reading digital ports values.
    """
    try:
        if request.method == "GET":
            value = str(phidget1011.get_digital_value(port))
            return Response(value, mimetype="application/json")
        else:
            content = request.get_json()
            result = phidget1011.set_digital_value(port, content['value'])
            return Response(result)
    except Exception as e:
        abort(404)

if __name__ == '__main__':
    app.run()
