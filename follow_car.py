#/usr/bin/python3

#import socket module
import socket
from Packet import Packet
import time
import threading

def main():

    ######## BEGIN SOCKET INITIALIZATION ########
    sndskt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)      #using ipv4 address + UDP packets
    recskt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)      #using ipv4 address + UDP packets
    sndskt.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)   #broadcasting for now but want to explore multicasting later on

    #need two sockets for p2p, configed in opposite manner
    listen_port = 6200
    send_port = 6201

    recskt.bind(("192.168.1.255", listen_port))                    #bind socket to local IP for listening
    sndskt.connect(("192.168.1.255", send_port))                   #connecting on the braodcast port
    ######## END SOCKET INITIALIZATION ########

    #spawn thread for listening
    list_thread = threading.Thread(target=listening, args=([recskt]))
    list_thread.start()

    bcast(sndskt)

def bcast(sskt):
    while(1): #replace with flag for getting new sample later on
        sskt.send(("Car 1 packet is broadcasting").encode())     #replace with packet encoding
        time.sleep(2)

def listening(rskt):
    print(rskt.getsockname())
    while(1):
        data, address = rskt.recvfrom(2048)
        print(address)
        if(address == "192.168.1.35"):
            print(data)

if __name__ == "__main__":
    main()