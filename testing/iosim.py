import socket
from binascii import hexlify

def parse_packet(packet: bytes):
    print("Parsed valid packet: " + hexlify(packet).decode())

def process_packet(packet: bytes):
    packet = packet[6:]
    parse_packet(packet)
    
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('127.0.0.1', 8080))
    s.listen()
    conn, addr = s.accept()
    with conn:
        while True:
            packet = conn.recv(1024)
            if not packet:
                break
            process_packet(packet)
