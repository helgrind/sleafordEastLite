from encodings import utf_8
import socket
from binascii import hexlify

def mb_crc16(data: str, poly: hex = 0xA001) -> str:
    '''
        CRC-16 MODBUS HASHING ALGORITHM
        From https://github.com/Kalebu/crc16-modbus-in-Python/blob/main/crc.py
    '''
    crc = 0xFFFF
    for byte in data:
        crc ^= byte
        for _ in range(8):
            crc = ((crc >> 1) ^ poly
                   if (crc & 0x0001)
                   else crc >> 1)

    hv = hex(crc).upper()[2:]
    blueprint = '0000'
    return (blueprint if len(hv) == 0 else blueprint[:-len(hv)] + hv)

def check_valid_packet(packet: bytes, cs: bytes) -> bool:
    """
    Check last two bytes are the CRC16 checksum
    """
    computed_cs = mb_crc16(packet)
    cs_str = hexlify(cs).upper().decode()
    return (cs_str == computed_cs)

def parse_packet(packet: bytes):
    print("Parsed valid packet: " + hexlify(packet).decode())

def process_packet(packet: bytes):
    cs = packet[-2:]
    packet = packet[:-2]
    if(check_valid_packet(packet, cs)):
        parse_packet(packet)
    else:
        print('CRC error!')

test_packet = b'\xff\xaa\x55\x11\x4c\xef'
process_packet(test_packet)

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#     s.bind(('127.0.0.1', 8080))
#     s.listen()
#     conn, addr = s.accept()
#     with conn:
#         while True:
#             packet = conn.recv(1024)
#             if not packet:
#                 break
#             process_packet(packet)