import sys
import socket

host=''
port=8081

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))

s.listen(5)
X = int(input("Enter # clients: "))
for  j in range(0,X):
	c,addr = s.accept()
	print("Got Connection from addr",addr)
	i=''
	while i!='exit':
                i=c.recv(1024).decode()
                print("recieved"+ i)
print("client"+str(j+1)+"connection closed")
c.close()

