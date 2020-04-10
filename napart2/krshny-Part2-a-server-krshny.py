import sys
import socket
host=''
port=8081

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))

s.listen(1)

c, addr=s.accept()

print ('got connection from ', addr)

i=''

while i != 'exit':
    i=c.recv(1024).decode()
    print (i)

c.close()
