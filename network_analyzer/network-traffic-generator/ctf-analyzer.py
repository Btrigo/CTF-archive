import socket
import time
import random
from scapy.all import IP, TCP, UDP, Raw, wrpcap

def generate_traffic(output_file, flag):
    packets = []
    
    # Common destination ports
    ports = [80, 443, 22, 21, 25, 53, 67, 68, 110, 143, 443, 445, 3389, 5900]
    
    # Generate normal traffic
    for _ in range(50):
        src_ip = f"192.168.{random.randint(1,255)}.{random.randint(1,255)}"
        dst_ip = f"192.168.{random.randint(1,255)}.{random.randint(1,255)}"
        
        # Random choice between TCP and UDP
        if random.choice([True, False]):
            packet = IP(src=src_ip, dst=dst_ip)/\
                    TCP(sport=random.randint(1024,65535), 
                        dport=random.choice(ports))/\
                    Raw(load=f"Regular traffic payload {random.randint(1,1000)}")
        else:
            packet = IP(src=src_ip, dst=dst_ip)/\
                    UDP(sport=random.randint(1024,65535), 
                        dport=random.choice(ports))/\
                    Raw(load=f"UDP datagram {random.randint(1,1000)}")
        
        packets.append(packet)
    
    # Insert flag in a random position
    flag_packet = IP(src=f"192.168.{random.randint(1,255)}.{random.randint(1,255)}",
                     dst=f"192.168.{random.randint(1,255)}.{random.randint(1,255)}")/\
                  TCP(sport=random.randint(1024,65535), dport=80)/\
                  Raw(load=f"CTF{{{flag}}}")
    
    packets.insert(random.randint(0, len(packets)), flag_packet)
    
    # Write packets to pcap file
    wrpcap(output_file, packets)
    print(f"Generated {len(packets)} packets and saved to {output_file}")
    print("Flag has been hidden in the traffic. Use Wireshark to find it!")

if __name__ == "__main__":
    flag = "flag:{you_found_the_flag}"
    generate_traffic("ctf_wireshark.pcap", flag)