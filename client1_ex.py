#/usr/bin/python3

#import socket module
import socket
import _thread

#create new socket and get host name
soc = socket.socket() #new socket
hname = socket.gethostname()

#need two sockets for p2p
listen_port = 6200
send_port = 6201

#bind socket to local host on the listening side
soc.bind((hname, listen_port))

#enables server to accept connections
soc.listen(2)

while True: #infinite loop of connection setting
    conn, addr = soc.accept()
    print("{} connected", addr)
    conn.send(str.encode("connected"))
    conn.close()
