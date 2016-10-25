import socket
import itertools

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ns = itertools.count(1)
na = itertools.ifilter(lambda x: x%2==0, ns)
for data in na:
    s.sendto(str(data), ('127.0.0.1', 9999))
    print s.recv(1024)

s.close()