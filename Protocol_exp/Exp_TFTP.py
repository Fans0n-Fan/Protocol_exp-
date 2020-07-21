#!/usr/bin/env python
import socket
host = '192.168.1.23'
port = 69

filename = "crash"
mode = "netascii"

data = "\x00\x02" + filename + "\x00" + mode + "\x00"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(data, (host, port))
s.close()
print "OK"