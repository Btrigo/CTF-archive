# Network Traffic Analysis Challenge

## Details

- difficulty: Easy
- category: Network Forensics
- files provided: ctf_wireshark.pcap
- flags: flag:{you_found_the_flag}

## Description

A network traffic capture contains suspicious communications between internal hosts. Can you analyze the traffic and find the hidden flag?

## Deployment

Run the Python script to generate the PCAP file with randomized traffic:

```bash
python ctf-analyzer.py
```
Open the generated PCAP file in wireshark:

```bash
wireshark ctf_wireshark.pcap
```


## Solution / Write up

1. Use Wireshark to analyze the network traffic.
2. Filter by protocols (TCP/UDP) to narrow down the search.
3. Examine packet payloads for suspicious content.
4. Look for patterns in communication between hosts.

## Hints
- Use display filters like tcp.port == 80 to focus on web traffic.
- Search through packet contents using strings like "CTF" or "flag".