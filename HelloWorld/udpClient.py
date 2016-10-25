import socket
import itertools

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ns = itertools.count(1)
for data in ns:
    s.sendto(str(data), ('127.0.0.1', 9999))
    print s.recv(1024)

s.close()