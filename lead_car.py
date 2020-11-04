#/usr/bin/python3

#import socket module
import socket
from Packet import Packet
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
    print("connected", addr)
    pkt = Packet(1, 0, 0)
    conn.send(pkt.encode_pkt())
    conn.close()
