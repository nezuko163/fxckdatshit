from socket import *
from conf import *

with socket(AF_INET, SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("connection")
    while True:
        msg = input()

        if msg:
            s.sendall(msg.encode("utf-8"))
            data = s.recv(1024)
            print(data.decode("utf-8"))

    # while True:
    #     string = input().encode("utf-8")
    #     s.sendall(string)
    #     data = s.recv(1024)
    #     print(data.decode("utf-8"))
