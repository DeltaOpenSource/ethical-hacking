from scapy.all import *

def scanPacket(packet):
    tcp_layer = packet['TCP']
    flags = tcp_layer.flags

    if flags == "FIN" or flags == "PSH" or flags == "URG":
        print("Xmas Scan Detected on Port ",tcp_layer.dport)

sniff(count=1000, filter="tcp", store =0, prn= scanPacket)
