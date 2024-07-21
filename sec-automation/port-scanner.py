print("CSN Script for Port Scanning!\n")

import socket

target = "127.0.0.1"
port_range = (75, 85)

open_ports = []

def scan_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    result = sock.connect_ex((target, port))
    
    if result == 0:
        open_ports.append(port)
        
    sock.close()

for port in range(port_range[0], port_range[1] + 1):
    print("Scanning port ", port)
    scan_port(port)

print("\n Open Ports:")

for port in open_ports:
    print(port)