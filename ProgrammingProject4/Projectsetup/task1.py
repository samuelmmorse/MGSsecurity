#!/usr/bin/env python3
from scapy.all import *

def print_pkt(pkt):
	pkt.show()

pkt = sniff(iface='br-85762f607e7f', filter='icmp and host 10.9.0.6 and dst port 23', prn=print_pkt)
