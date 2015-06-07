from flask import Flask, Response
from ciscophidget import Module1011

app = Flask(__name__)
phidget1011 = Module1011("10.10.10.250", "0022bdcf4574")

@app.route('/api/v1/analog/<int:port>')
def api_read_analog(port):
    value = str(phidget1011.get_analog_value(port))
    return Response(value, mimetype="application/json")

if __name__ == '__main__':
    app.run()
