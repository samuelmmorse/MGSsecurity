#!/usr/bin/env python3
from scapy.all import *

def print_pkt(pkt):
	pkt.show()

pkt = sniff(iface='br-85762f607e7f', filter='icmp', prn=print_pkt)
