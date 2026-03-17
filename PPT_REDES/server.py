# Servidor
import socket

HOST = "0.0.0.0"
PORT = 9006

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    
    s.listen(1)
    print("[Server] Aguardando Jogador 1...")
    conn1, addr1 = s.accept()
    conn1.sendall("[Server] Ok. Você é o Jogador 1".encode('utf-8'))
    conn1.sendall("[Server] Aguardando Jogador 2".encode('utf-8')) 

    print("[Server] Aguardando Jogador 2...")

    conn2, addr2 = s.accept()    
    conn2.sendall("[Server] Ok. Você é o Jogador 2".encode('utf-8'))
    conn2.sendall("[Server] Aguardando Jogador 1 ".encode('utf-8'))

    while True:
        conn1.sendall("[Server] Faça a sua jogada: ".encode('utf-8'))
        msg1 = conn1.recv(1024).decode('utf-8')
        print("[Jogador 1] jogou" , msg1)

        conn2.sendall("[Server] Faça a sua jogada: ".encode('utf-8'))
        msg2 = conn2.recv(1024).decode('utf-8')
        print("[Jogador 2] jogou" , msg2)

        if(msg1 == "pedra"):
         if(msg2 == "papel"):
            conn1.sendall("[Server] Você perdeu!".encode('utf-8'))
            conn2.sendall("[Server] Você ganhou!".encode('utf-8'))
        if(msg2 == "tesoura"):
            conn1.sendall("[Server] Você ganhou!".encode('utf-8'))
            conn2.sendall("[Server] Você perdeu!".encode('utf-8'))
        if(msg2 == "pedra"):
            conn1.sendall("[Server] Empate!".encode('utf-8'))
            conn2.sendall("[Server] Empate!".encode('utf-8'))
        elif(msg1 == 'tesoura'):
         if(msg2 == "papel"):
            conn1.sendall("[Server] Você ganhou!".encode('utf-8'))
            conn2.sendall("[Server] Você perdeu!".encode('utf-8'))
        if(msg2 == "tesoura"):
            conn1.sendall("[Server] Empate!".encode('utf-8'))
            conn2.sendall("[Server] Empate!".encode('utf-8'))
        if(msg2 == "pedra"):
            conn1.sendall("[Server] Você perdeu!".encode('utf-8'))
            conn2.sendall("[Server] Você ganhou!!".encode('utf-8'))
        else:
            if(msg2 == "papel"):
             conn1.sendall("[Server] Empate!".encode('utf-8'))
             conn2.sendall("[Server] Empate!".encode('utf-8'))
            if(msg2 == "tesoura"):
             conn1.sendall("[Server] Você perdeu!".encode('utf-8'))
             conn2.sendall("[Server] Você ganhou!".encode('utf-8'))
        if(msg2 == "pedra"):
            conn1.sendall("[Server] Você ganhou!".encode('utf-8'))
            conn2.sendall("[Server] Você perdeu!".encode('utf-8'))

 