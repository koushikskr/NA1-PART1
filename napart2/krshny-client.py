import socket
host = '192.168.86.42'
port = 12029

def connect(host,port):
	serv=socket.socket()
	serv.connect((host,port))
	return serv

def readinput():
	msg=input("Me: ")
	return msg

def exchange_messages(m,serv):
	while True:
		if m == "Hello From Client Koushik":
			serv.send(str.encode(m))
			message=str(serv.recv(12006).decode())
			print("Server:" + message)
			m=readinput()
		elif m == "Exit":
			serv.send(str.encode(m))
			message=str(serv.recv(1200).decode())
			print("Server: " + message)
			if(message == "Exit"):
				break
			else:
				m=readinput()
		else:
			serv.send(str.encode(m))
			message=str(serv.recv(12006).decode())
			print("Server:"+ message)
			m=readinput()

def main():
	serv=connect(host,port)
	print("Enter message here...")
	m=input("Me: ")
	exchange_messages(m,serv)
	serv.close()

if __name__== "__main__":
	main()
