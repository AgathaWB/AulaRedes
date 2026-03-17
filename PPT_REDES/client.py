# Cliente
import socket

HOST = "192.168.248.108"
PORT = 9009

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(s.recv(1024).decode())
    print(s.recv(1024).decode())
    while True:   
        print(s.recv(1024).decode())
        msg = input()
        s.sendall(msg.encode('utf-8'))
        print(s.recv(1024).decode())