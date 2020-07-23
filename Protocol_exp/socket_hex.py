#!/usr/bin/env python
import socket

port = 8291
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('192.168.199.117',port))
d = '2706e26df8c01'
d = d.decode('hex')
s.send(d)
r = s.recv(100)
#print r
print r.encode('hex')



