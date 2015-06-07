# coding: utf-8
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import os
from flask import Flask, Response, request, abort
from ciscophidget import Module1011

# The correct values should be defined on environment variables.
USBIP_SERVER = os.environ.get("USBIP_SERVER")
EIOT_MACADDRESS = os.environ.get("EIOT_MACADDRESS")

app = Flask(__name__)
phidget1011 = Module1011(USBIP_SERVER, EIOT_MACADDRESS)

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
