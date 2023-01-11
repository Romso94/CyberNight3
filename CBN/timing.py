#!/usr/bin/python3.10
import sys
from socket import socket
import time
import time
import random
import os

sock = socket()
# connection to hostname on the port.
sock.connect(('10.242.0.1',10003))
random.seed(int(time.time()))

# Receive no more than 1024 bytes

tm = sock.recv(1024)

print(tm)


true_num_1 = random.randint(0, 50)

sock.send(f"{str(true_num_1)}\n".encode())

tm = sock.recv(1024)

print(tm)


true_num_2 = random.randint(0, 50000000000)

sock.send(f"{str(true_num_2)}\n".encode())


true_num_3 = random.random()

sock.send(f"{str(true_num_3)}\n".encode())

tm =sock.recv(1024)
tm = sock.recv(1024)

print(tm)


