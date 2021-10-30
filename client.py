from threading import Thread 
import socket 
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("127.0.0.1",6801))
def reciver(client):
    while True:
        msg = client.recv(1024)
        msg = msg.decode("utf-8")
        if not msg:
            print("CLOSED")
            break
        print(f"Recive:{msg}") 
def writer(client):
    while True:
        msg = input("->")
        msg = msg.encode()
        client.send(msg)
Reciver = Thread(target=reciver,args=[client])
Writer = Thread(target=writer,args=[client])
Reciver.start()
Writer.start()
Reciver.join()
Writer.join()
client.close()