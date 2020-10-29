#/usr/bin/python3

#import socket module
import socket
import _thread

#create new socket and get host name
soc = socket.socket() #new socket
hname = socket.gethostname()

#need two sockets for p2p, configed in opposite manner
listen_port = 6201
send_port = 6200

#bind socket to local host on the listening side
soc.bind((hname, listen_port))

soc.connect((hname, send_port))
print(soc.recv(1024).decode())