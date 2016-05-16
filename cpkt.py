#!/usr/bin/python

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Simple wrapper for scapy to send crafted packet from a supplied
MAC address for network testing

Usage:
sudo ./craftedpkt.py <SRC_MAC> <DST_MAC> <ETHERTYPE> <IF_NAME>

Example:
sudo ./craftedpkt.py 00:00:00:00:00:01 00:00:00:00:00:02 0x800 eth1
"""

import sys
#*** Scapy for sending/receiving packets:
from scapy.all import Raw, Ether, sendp

#*** Must have 5 parameters passed to it (first parameter is script)
assert len(sys.argv) == 5

#*** Get parameters from command line
SRC_MAC = sys.argv[1]
DST_MAC = sys.argv[2]
ETH_TYPE = sys.argv[3]
IF_NAME = sys.argv[4]

HEX_ETH_TYPE = int(ETH_TYPE, 16)

crafted_packet = Ether(src=SRC_MAC, dst=DST_MAC, type=HEX_ETH_TYPE)

sendp(crafted_packet, iface=IF_NAME)
