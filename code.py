import socket
import threading
import os

port = 5050
buffer_size = 1024
server_ip = socket.gethostbyname(socket.gethostname())
addr_server = (server_ip, port)
format = "utf-8"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(addr_server)

def client_handle(conn, addr_client):
    print(f"NEW CONNECTION == {addr_client}")
    connected = True
    while connected:
        msg = conn.recv(buffer_size).decode(format)
        if msg == "cookie":
            os.open(r"D:\python\PycharmProjects\helloworld\.py files\Black_board\cookie.txt")
        else:
            print(f"{addr_client} - {msg}")
            conn.send("msg recieved\n".encode(format))

def start():
    server.listen()
    print(f"SERVER IS LISTENING ON {server_ip}")
    while True:
        conn, addr_client = server.accept()
        thread = threading.Thread(target=client_handle, args=(conn, addr_client))
        thread.start()
        print(f"ACTIVE CONNECTIONS == {threading.active_count() - 1}")

print("SERVER IS STARTING")
start()
