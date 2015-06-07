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
from time import sleep
from zeus import client
from ciscophidget import Module1011

# The correct values should be defined on environment variables.
USBIP_SERVER = os.environ.get("USBIP_SERVER")
EIOT_MACADDRESS = os.environ.get("EIOT_MACADDRESS")
ZEUS_USERTOKEN = os.environ.get("ZEUS_USERTOKEN")

print("DEBUG-INIT: Initializing the EIoT device.")
phidget1011 = Module1011(USBIP_SERVER, EIOT_MACADDRESS)
print("DEBUG-INIT: Connecting to Cisco Zeus platform.")
zeus = client.ZeusClient(ZEUS_USERTOKEN, 'api.ciscozeus.io')

count = 0
while True:
    print("DEBUG-COUNT%d: Getting analog values." % count)
    analog0 = phidget1011.get_analog_value(0)
    analog1 = phidget1011.get_analog_value(1)
    print("DEBUG-COUNT%d: Got A0=%s and A1=%s." % (count, analog0, analog1))
    print("DEBUG-COUNT%d: Sending values to Cisco Zeus." % count)
    metrics = [{"point":{"analog0":analog0,"analog1":analog1}}]
    zeus.sendMetric("eiot-phidget1011", metrics)
    print("DEBUG-COUNT%d: Waitig for the next iteraction (1s)." % count)
    sleep(1)
    count += 1
