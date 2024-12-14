
#--------------------------------------------------

import socket
import ssl
import os
import argparse

#--------------------------------------------------

SERVER_PORT = 8443
MAX_MESSAGE_SIZE = 1024

#--------------------------------------------------

def start_client(certfile_path):
    context = ssl.create_default_context()
    context.load_verify_locations(certfile_path)

    with socket.create_connection(("localhost", SERVER_PORT)) as sock:
        with context.wrap_socket(sock, server_hostname="localhost") as tls_sock:
            tls_sock.sendall(b"hello, server!")
            data = tls_sock.recv(MAX_MESSAGE_SIZE)
            print(f"received: {data.decode()}")
            while True:
                message = input("> ")
                tls_sock.sendall(message.encode())
                if message.lower() == "disconnect":
                    break
                print("server is typing...")
                data = tls_sock.recv(MAX_MESSAGE_SIZE)
                print(f"received: {data.decode()}")

#--------------------------------------------------

if __name__ == "__main__":
    os.environ['SSLKEYLOGFILE'] = 'ssl_logs.txt'

    start_client("cert.pem")

#--------------------------------------------------
