import socket

# parameters
host_ip = 'localhost'
port_no = 8080

def connect(host_ip,port_no):
	s=socket.socket()
	s.connect((host_ip, port_no))
	return s

def exchange_messages(m,s):
	while True:
		if m == "Bye from Client-koushik":
			s.send(str.encode(m))
			data=str(s.recv(1024).decode())
			print(data)
			if(data == "Bye from Server-koushik"):
				break
			else:
				m=input('Enter another message here --> ')

		elif m == "Hello from Client-koushik":
			s.send(str.encode(m))
			data=str(s.recv(1024).decode())
			print(data)
			m=input("Enter another message here -->")
		else:
			s.send(str.encode(m))
			data=str(s.recv(1024).decode())
			print(data)
			m=input("Enter standard messages -->")

def main():
	s=connect(host_ip, port_no)
	m=input("Enter message here -->")
	exchange_messages(m,s)
	s.close()

if __name__== "__main__":
	main()
