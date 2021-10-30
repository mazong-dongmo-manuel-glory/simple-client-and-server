import socket
from threading import Thread
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
def reciver(client,ip):
    while True:
        msg = client.recv(1024)
        msg = msg.decode("utf-8")
        if not msg:
            print("CLOSED")
            break
        print(f"{msg}:{ip}")
def writer(client,ip):
    while True:
        msg = input("->")
        msg = msg.encode()
        client.send(msg)
server.bind(("127.0.0.1",6801))
server.listen(1)
client,ip = server.accept()

Reciver = Thread(target=reciver,args=[client,ip])
Writer = Thread(target=writer,args=[client,ip])
Reciver.start()
Writer.start()
Reciver.join()
Writer.join()
print("END OF WORK")
client.close()
server.close()
 
