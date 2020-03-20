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

def transfer_data(c):
	while True:
		data=c.recv(1026)
		if str(data.decode()) == "exit":
			c.send(str.encode("server gone"))
			print(str(data.decode()))
			break		
		else:
			with open('output.txt', 'wb') as fp:
				while True:
					print(data)
					fp.write(data)
					if str(data).find("File transfer complete") != -1:
						fp.write(str.encode("\n This line was added by me in the Server !!! \n"))
						print("\n This line was added by me in the Server !!! \n")
						break
					data = c.recv(1026)

			fp = open('output.txt','rb')
			chunk = fp.read(1025)
			while (chunk):
				c.send(chunk)
				chunk = fp.read(1026)
			fp.close()
			c.send(str.encode("File sent back from server"))

def main():
	c=bind(host_ip, port_no)
	transfer_data(c)
	c.close()

if __name__== "__main__":
	main()