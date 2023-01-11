import sys
from socket import socket
import time

keyword = "CYBN"
sock = socket()
# connection to hostname on the port.
sock.connect(('10.242.0.1',10002))

# Receive no more than 1024 bytes
tm = sock.recv(1024)
truc = tm.decode().split("\n")
    

print(tm)


print(f"Envoie de : {truc[1]}\n".encode())

sock.send(f"{truc[1]}\n".encode())
tm = sock.recv(1024)

truc = tm.decode().split("\n")
    

print(tm)


print(f"Envoie de : {truc[1]}\n".encode())

sock.send(f"{truc[1]}\n".encode())
tm = sock.recv(1024)

while True:    
    
    truc = tm.decode().split("\n")
    

    print(tm)


    print(f"Envoie de : {truc[0]}\n".encode())

    sock.send(f"{truc[0]}\n".encode())

    tm = sock.recv(1024)



   

    #if keyword in tm.decode("utf-8"):
     #   break

    # if tm.decode("utf-8")=="123456789":
    #     sock.send(123456789)

    # # send a thank you message to the client.
    # else:
    #     sock.send(tm.decode('utf-8'))
    # tm = sock.recv(20000)

# close the client socket
sock.close()