import socket
import threading
from time import sleep

HOST = "0.0.0.0"
PORT = 9002

LETRA = ''

semaforo = threading.Semaphore(0)

def atender_cliente(conn, addr):
    semaforo.acquire()
    with conn:
     conn.sendall(LETRA.encode())
    

def iniciar_servidor():
    global LETRA
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen()

        print(f"Servidor ouvindo em {HOST}:{PORT}")

        #Aguardando jopgador 1
        conn_1, addr_1 = server.accept()#parado esperando
        thread_1 = threading.Thread(target=atender_cliente, args=(conn_1, addr_1), daemon=True)
        thread_1.start()

        #Aguardando jogador 2
        conn_2, addr_2 = server.accept()#parado esperando
        thread_2 = threading.Thread(target=atender_cliente, args=(conn_2, addr_2), daemon=True)
        thread_2.start()

        #sorteia a letra
        LETRA = 'T'
        #libera o semaforo
        semaforo.release()
        semaforo.release()

        thread_1.join()
        thread_2.join()

if __name__ == "__main__":
    iniciar_servidor()
    
