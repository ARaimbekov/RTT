import pyshark

if __name__ == '__main__':
    capture = pyshark.LiveCapture(interface='Ethernet 3', bpf_filter='tcp port 443')
    capture.sniff(timeout=10, packet_count=5)
    for packet in capture:
        print(packet)