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
Simple wrapper for scapy to send crafted TCP SYN packet for network testing

Usage:
sudo ./cpkt.py <SRC_MAC> <DST_MAC> <ETHERTYPE> <SRC_IP> <DST_IP> <SRC_PORT> <DEST_PORT> <IF_NAME> <REPEAT_INTERVAL> <COUNT>

Example:
sudo ./cpkt.py 00:00:00:00:12:34 08:00:27:c8:db:91 0x800 10.1.2.3 10.1.0.2 1234 5678 eth1 0.01 200

This could be a lot more extensible if had time, just built for a single use case at this stage...
"""

import sys
#*** Scapy for sending/receiving packets:
from scapy.all import Raw, Ether, sendp, IP, TCP

import time

#*** Must have 10 parameters passed to it (first parameter is script)
assert len(sys.argv) == 11

#*** Get parameters from command line
SRC_MAC = sys.argv[1]
DST_MAC = sys.argv[2]
ETH_TYPE = sys.argv[3]
SRC_IP = sys.argv[4]
DST_IP = sys.argv[5]
SRC_PORT = int(sys.argv[6])
DST_PORT = int(sys.argv[7])
IF_NAME = sys.argv[8]
REPEAT_INTERVAL = float(sys.argv[9])
REPEAT_COUNT = int(sys.argv[10])

HEX_ETH_TYPE = int(ETH_TYPE, 16)

crafted_packet = Ether(src=SRC_MAC, dst=DST_MAC, type=HEX_ETH_TYPE)/ \
                    IP(src=SRC_IP, dst=DST_IP, proto=6)/ \
                    TCP(sport=SRC_PORT, dport=DST_PORT, flags='S')

finished = 0
count = 0
while not finished:
    sendp(crafted_packet, iface=IF_NAME)
    time.sleep(REPEAT_INTERVAL)
    count += 1
    if count >= REPEAT_COUNT:
        finished = 1
