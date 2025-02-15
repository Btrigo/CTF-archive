from scapy.all import sniff

# Define the flag
FLAG = "flag{sniff_the_network}"

def process_packet(packet):
    # Check for a specific protocol or field
    if packet.haslayer("IP") and packet["IP"].src == "192.168.1.1":  # Example condition
        print(f"Captured packet: {packet.summary()}")
        print(f"The flag is: {FLAG}")

# Start sniffing
print("Packet sniffer started. Listening for packets...")
sniff(prn=process_packet, filter="ip", count=10)  # Adjust the filter and count as needed
