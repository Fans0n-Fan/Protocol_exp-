#!/usr/bin/env python
import socket
host = '192.168.1.23'
port = 21

def receive_banner(socket):
    socket.recv(1024)
user = "anonymous"
passwd = "anonymous@abcd.com"
command = ""
payload = ""

data1 = "USER " + user + "\r\n"
data2 = "PASS " + passwd + "\r\n"

data3 = command + payload
s = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
s.connect((host, port))
receive_banner(s)

s.send(data1)
s.recv(2048)

s.send(data2)
s.recv(2048)

s.send(data3)
s.close()
print "OK"