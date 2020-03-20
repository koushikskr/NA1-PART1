import socket

# parameters
host_ip = ''
port_no = 8080

def bind(host_ip,port_no):
	s=socket.socket()
	s.bind((host_ip, port_no))
	print('listening ...')
	s.listen(1)
	c,addr = s.accept()
	return c

def exchange_messages(c):
	while True:
		data=str(c.recv(1024).decode())
		if data == "Bye from Client-koushik":
			print(data)
			c.send(str.encode("Bye from Server-koushik"))
			break
		elif data == "Hello from Client-koushik":
			print(data)
			c.send(str.encode("Hello from Server-koushik"))
		else:
			print(data)
			c.send(str.encode(data))
	
def main():
	c=bind(host_ip, port_no)
	exchange_messages(c)
	c.close()

if __name__== "__main__":
	main()
