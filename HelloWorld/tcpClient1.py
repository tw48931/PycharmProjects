import socket
import itertools

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.6.12.34', 9999))
ns = itertools.count(1)
na = itertools.takewhile(lambda x: x<100, ns)
for x in na:
    s.send(str(x))
    print s.recv(1024)

s.send('exit')
s.close()