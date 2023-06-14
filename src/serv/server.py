from socket import *
from conf import *
import selectors


def handle(sock, addr) -> bool:
    try:
        data = sock.recv(1024)
    except ConnectionError:
        print("client disconnected while receiving data")
        return False

    if data:
        print(f"received {data.decode('utf-8')} from {addr}")

    else:
        print(f"disconnected by {addr}")
        return False

    try:
        sock.sendall(data)
    except ConnectionError:
        print(f"client {addr}"
              f"disconnected before getting data")
        return False

    return True


if __name__ == '__main__':
    with socket(AF_INET, SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen(1)
        inputs = [server]
        outputs = []

        while True:
            readable, writable, exceptional = select(inputs, outputs, inputs)

            for socket in readable:
                if socket == server:
                    sock, addr = server.accept()
                    print("connected by", addr)
                    inputs.append(sock)

                else:
                    addr = socket.getpeername()

                    if not handle(socket, addr):
                        inputs.remove(socket)

                        if socket in outputs:
                            outputs.remove(socket)
                        socket.close()












    # lst = [s.accept() for _ in range(2)]
    # [print(i[0]) for i in lst]

    # with conn:
    #     print(f"connected by {addr}")
    #     while True:
    #         data = conn.recv(1024)
    #         conn.sendall(data)
