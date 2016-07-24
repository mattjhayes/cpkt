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
Simple wrapper for scapy to send crafted ICMP echo for network testing

Usage:
sudo ./cpkt.py <SRC_MAC> <DST_MAC> <SRC_IP> <DST_IP> <IF_NAME> <REPEAT_INTERVAL> <COUNT>

Example:
sudo ./cpkt.py 00:00:00:00:12:34 08:00:27:c8:db:91 10.1.2.3 10.1.0.2 eth1 0.01 200

This could be a lot more extensible if had time, just built for a single use case at this stage...
"""

import sys
#*** Scapy for sending/receiving packets:
from scapy.all import Raw, Ether, sendp, IP, TCP

import time

#*** Must have 10 parameters passed to it (first parameter is script)
assert len(sys.argv) == 8

#*** Get parameters from command line
SRC_MAC = sys.argv[1]
DST_MAC = sys.argv[2]
SRC_IP = sys.argv[3]
DST_IP = sys.argv[4]
IF_NAME = sys.argv[5]
REPEAT_INTERVAL = float(sys.argv[6])
REPEAT_COUNT = int(sys.argv[7])

data = "blahblahblah"
# define ip and icmp
eth = Ether()
eth.src=SRC_MAC
eth.dst=DST_MAC
ip = IP()
ip.src = SRC_IP
ip.dst = DST_IP
icmp = ICMP()
icmp.type = 8
icmp.code = 0

finished = 0
count = 0
while not finished:
    sendp(eth/ip/icmp/data, iface=IF_NAME)
    time.sleep(REPEAT_INTERVAL)
    count += 1
    if count >= REPEAT_COUNT:
        finished = 1
