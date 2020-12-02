#/usr/bin/python3

"""
Example code for exchanging packets through a broadcast address
Currently being used for communication between multiple debian based SBCs on an adhoc network 
Last revision: December 2nd, 2020
"""

import socket
import sys
from Packet import Packet
import time
import threading

def main():
 
    if(len(sys.argv) != 3):                                        #checking argument validity 
        print("Incorrect number of arguments")
        print("Must specify index for sending and receiving port")
        sys.exit()

    ls = int(sys.argv[1])                                          #for mapping sending port
    sn = int(sys.argv[2])                                          #for mapping listening port

    send_port_map = {1: 6201, 2: 6202, 3: 6303, 4: 6404}
    recv_port_map = {1: 6201, 2: 6202, 3: 6303, 4: 6404}

    ######## BEGIN SOCKET INITIALIZATION ########
    sndskt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)      #using ipv4 address + UDP packets
    recskt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)      #using ipv4 address + UDP packets
    sndskt.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)   #broadcasting for now but want to explore multicasting later on

    #Port definitions need to be configured per car
    listen_port = send_port_map[ls]
    send_port = recv_port_map[sn]

    recskt.bind(("100.100.5.255", listen_port))                    #bind socket to broadcast for listening
    sndskt.connect(("100.100.5.255", send_port))                   #connecting on the braodcast port
    ######## END SOCKET INITIALIZATION ########

    #spawn thread for listening
    list_thread = threading.Thread(target=listening, args=([recskt]))
    list_thread.start()

    #Broadcast data
    bcast(sndskt)

def bcast(sskt):
    while(1):                                                      #replace with flag for getting new sample later on
        spkt = Packet(1, 0, 1)                                     #test packet 
        sskt.send((spkt.build_str()).encode())                     #replace with packet encoding
        time.sleep(2)

def listening(rskt):
    rpkt = Packet(0, 0, 0)                                         #initializing packet
    print(rskt.getsockname())
    while(1):
        data, address = rskt.recvfrom(200)
        rpkt.decode_pkt(data)
        printPkt(rpkt, address)

def printPkt(pkt, address):
    print(f"{address}, {pkt.identifier}, {pkt.steering}, {pkt.speed}\n")

if __name__ == "__main__":
    main()
