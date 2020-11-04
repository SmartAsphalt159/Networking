#/usr/bin/python3

#import socket module
import socket
from Packet import Packet
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

recpkt = Packet(0, 0, 0)

recpkt.decode_pkt(soc.recv(1024))
print(recpkt.identifier, recpkt.steering, recpkt.speed)