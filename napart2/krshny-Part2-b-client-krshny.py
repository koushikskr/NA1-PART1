import sys
import socket

host='localhost'
port=8081

def connect(host,port):
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    return s

def main():
    s=connect(host,port)
    message=""

    
    while message != 'exit':
        message= input("Type Message\n")
        s.send(str.encode(message))
    s.close()
    print ("connection closed")

if __name__== "__main__":
    main()




