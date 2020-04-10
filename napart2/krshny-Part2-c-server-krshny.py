import socket
import threading
from _thread import start_new_thread
# parameters
host_ip='localhost'
port_no=8080

def bind(host_ip,port_no):
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host_ip,port_no))
	s.listen(5)
	return s


def client_thread(c,addr):
    print ("got connection from", addr)
    i=""
    while i != "exit":
        i=c.recv(1024).decode()
        print ("received", addr, i)
    print ("client connection closed", addr)
    c.close()


def main():
	s=bind(host_ip, port_no)
	while True:
		c,addr=s.accept()
		start_new_thread(client_thread,(c,addr,))
	print ("connection closed with all the clients\n")
	s.close()


if __name__== "__main__":
	main()
