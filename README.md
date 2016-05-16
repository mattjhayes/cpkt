# cpkt
Send a crafted packet

A very basic wrapper around *scapy* to send a crafted packet from the command line.

## Usage:
```
sudo ./cpkt.py <SRC_MAC> <DST_MAC> <ETHERTYPE> <IF_NAME>
```

## Example:
```
sudo ./cpkt.py 00:00:00:00:00:01 00:00:00:00:00:02 0x800 eth1
WARNING: No route found for IPv6 destination :: (no default route?)
.
Sent 1 packets.
```
