from scapy.all import *
a = IP()
dest = '8.8.8.8'
a.dst = dest
b = ICMP()
a.ttl = 1
while (a.ttl < 100):
	reply = sr1(a/b, verbose=0, timeout=2)
	
	if (reply == None):
		print(str(a.ttl) + "\t* * * *")
		a.ttl += 1
		continue
	print(str(a.ttl) + "\t" + reply.src)
	if (reply.src == dest):
		break
	a.ttl +=1
	







#packet = Ether()/IP(dst='10.9.0.6')/TCP(dport=23,flags='S')
#send(packet)

