import time
import socket

class Interfaces:
    def __init__(self, app) -> None:
        self.app = app
        self.ADDRESS = ('127.0.0.1', 8080)
        
    def connect(self) -> None:
        self.conn.connect(('127.0.0.1', 8080))

    def update(self) -> None:
        try:
            self.conn.sendall(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
            print('Sent IO packet')
        except:
            self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.conn.connect(self.ADDRESS)
            print('Reconnected to interface.')
            self.conn.sendall(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
            print('Sent IO packet')
        