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
from ciscophidget import Module1011

# The correct values should be defined on environment variables.
USBIP_SERVER = os.environ.get("USBIP_SERVER")
EIOT_MACADDRESS = os.environ.get("EIOT_MACADDRESS")

phidget1011 = Module1011(USBIP_SERVER, EIOT_MACADDRESS)

while True:
    print phidget1011.get_analog_value(0), phidget1011.get_analog_value(1)
