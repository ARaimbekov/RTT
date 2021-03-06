import pyshark
import nmap

proxy_ip = '142.4.203.248'

if __name__ == '__main__':
    capture = pyshark.LiveCapture(interface='Ethernet 3', bpf_filter='tcp port 443')
    capture.sniff(timeout=5, packet_count=3)
    for packet in capture:
        print('Destination:', packet.ip.dst)
        print('Ack:', packet.tcp.flags_ack)
        print('Syn:', packet.tcp.flags_syn)
        print('Seg:', packet.tcp.seq)
        print('Source:', packet.ip.src)
        print("***********************")

    capture_proxy = pyshark.LiveCapture(interface='Ethernet 3', bpf_filter='tcp port 3128')
    capture_proxy.sniff(timeout=5, packet_count=3)
    for packet in capture_proxy:
        print('Destination:', packet.ip.dst)
        print('Ack:', packet.tcp.flags_ack)
        print('Syn:', packet.tcp.flags_syn)
        print('Seq:', packet.tcp.seq)
        print('Source:', packet.ip.src)
        print("***********************")

    scanner = nmap.PortScanner()
    scanner.scan(proxy_ip, '-v', '-sS')
    print(scanner.scaninfo())
    print('Ip_Status :', scanner[proxy_ip].state())
    print('Open Ports: ', scanner[proxy_ip]['tcp'].keys())