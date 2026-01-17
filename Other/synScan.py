import sys
from scapy.all import IP, ICMP, TCP, sr1

def icmp_probe(ip):
    icmp_packet = IP(dst=ip)/ICMP()
    resp_packet = sr1(icmp_packet, timeout=10)
    return resp_packet

def syn_scan(ip, port):
    syn_packet = IP(dst=ip)/TCP(dport=port, flags='S')
    response = sr1(syn_packet, timeout=1, verbose=0)
    return response

if __name__ == "__main__":
    ip = sys.argv[1]
    port = int(sys.argv[2])

    if icmp_probe(ip):
        print("[+] The host is connected to the network")
        scan_results = syn_scan(ip, port)
        if scan_results:
            print("[*] Scan results:")
            scan_results.show()
        else:
            print("[-] No response from port")
    else:
        print("[-] The host is not connected to the network")
