from scapy.all import *
a = IP()
a.show()

# python3 mycode.py
###[ IP ]###



packet = Ether()/IP(dst='10.9.0.6')/TCP(dport=23,flags='S')

send(packet)
print(packet)
