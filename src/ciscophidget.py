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
import usb.core

class Module1011:
    """
    Class to encapsulate the methods and interfaces for the Phidget module 1011,
    an USB Analog/Digital interface capable of 2 analog in and 2 digital in/out.
    """

    def __init__(self, usbip_server, eiot_mac, debug=False):
        """
        Initialization method for the class.
        """
        if debug:
            print " * Initializing EIoT %s@%s..." % (eiot_mac, usbip_server)
        os.environ["USBIP_SERVER"] = usbip_server
        self.device = usb.core.find(address=int(eiot_mac, 16))
        if self.device is None:
            raise ValueError('EIoT device %s not found.' % eiot_mac)
        self.endpoint = self.device[0][(0,0)][0]
        self.device.set_configuration()
        if debug:
            print " * ...done!"

    def __normalize_analog__(self, raw_value):
        """
        Method to normalize the analog reading data.
        """
        return int(raw_value/4.096)

    def get_analog_value(self, port):
        """
        Read analog value from port numbered "port".
        """
        if port not in [0,1]:
            raise ValueError("Port number should be 0 or 1.")
        data = self.device.read(1, self.endpoint.wMaxPacketSize)
        if port == 0:
            data0 = (data[0x0b] | ((data[0x0c] & 0xf0) << 4))
            return self.__normalize_analog__(data0)
        else:
            data1 = (data[0x0d] | ((data[0x0c] & 0x0f) << 8))
            return self.__normalize_analog__(data1)

    def get_digital_value(self, port):
        """
        Read digital value from port numbered "port".
        """
        raise Exception("Not implemented.")

    def set_digital_value(self, port, value):
        """
        Write digital valure at port numbered "port".
        """
        raise Exception("Not implemented.")
