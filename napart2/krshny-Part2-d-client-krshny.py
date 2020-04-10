import sys
import socket
import _thread
from _thread import start_new_thread

# parameters
host_ip = 'localhost'
port_no = 8082

def connect(host_ip,port_no):
	s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host_ip,port_no))
	return s

def client(s):
    while 1:
        z=s.recv(1024)
        if not z: break
        print(z.decode())
        #z=s.recv(1024).decode()
        #print(z)

def connect_client(s):
	message=""
	start_new_thread(client, (s,))
	while message !="exit":
		message=input("enter message:\n")
		s.send(str.encode(message))
	s.close()
	print ("connection closed")
	

def main():
	s=connect(host_ip, port_no)
	connect_client(s)
	s.close()

if __name__== "__main__":
    main()
