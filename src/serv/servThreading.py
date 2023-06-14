from socketserver import ThreadingTCPServer
from socketserver import BaseRequestHandler

from conf import *


class ConnectionHandler(BaseRequestHandler):
    def handle(self):
        print("Connected by", self.client_address)
        while True:
            try:
                data = self.request.recv(BUFFSIZE_FOR_INT_FROM_0_TO_65535)
                print(f"user {self.client_address} send message: {int.from_bytes(data, 'little')}")
            except ConnectionError:
                print("client have disconnected before get message")
                break

            if not data:
                break

            try:
                self.request.sendall(data)
            except ConnectionError:
                print("client have disconnected after send message")
                break

        print("disconneted by", self.client_address)


if __name__ == '__main__':
    with ThreadingTCPServer((HOST, PORT), ConnectionHandler) as server:
        server.serve_forever()

    while True:
        print(input())
