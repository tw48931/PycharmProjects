import socket
import itertools

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.6.12.34', 9999))
print s.recv(1024)
for x in itertools.count(1):
    s.send(str(x))
    print s.recv(1024)

s.send('exit')
s.close()