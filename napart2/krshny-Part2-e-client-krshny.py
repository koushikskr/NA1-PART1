import sys
import socket

host='localhost'
port=8080

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

message = ""
while message != "exit":
	message=input("Type Message \n")
	s.send(str.encode(message))

s.close()
print("Connection Closed")
