
#--------------------------------------------------

import socket
import ssl
import os
import argparse

#--------------------------------------------------

SERVER_PORT = 8443
MAX_CLIENTS_COUNT = 5
MAX_MESSAGE_SIZE = 1024

#--------------------------------------------------
# однопоточный сервер, всех обрабатывает по очереди
# сообщение disconnect прерывает соединение

def start_server(cert_path, key_path):
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile=cert_path, keyfile=key_path)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
        sock.bind(("localhost", SERVER_PORT))
        sock.listen(MAX_CLIENTS_COUNT)
        with context.wrap_socket(sock, server_side=True) as tls_sock:
            while True:
                connection, addr = tls_sock.accept()
                with connection:
                    print(f"connected by {addr}")
                    data = connection.recv(MAX_MESSAGE_SIZE)
                    print(f"received: {data.decode()}")
                    connection.sendall(b"hello, client!")
                    while True:
                        print("client is typing...")
                        data = connection.recv(MAX_MESSAGE_SIZE)
                        print(f"received: {data.decode()}")
                        if data.decode().lower() == "disconnect":
                            break
                        connection.sendall(input("> ").encode())
                    print(f"{addr} disconnected")

#--------------------------------------------------

if __name__ == "__main__":
    os.environ['SSLKEYLOGFILE'] = 'ssl_logs.txt'

    start_server("cert.pem", "key.pem")

#--------------------------------------------------