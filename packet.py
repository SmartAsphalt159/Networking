#/usr/bin/python3

#class for packet structure

import socket

class packet:

    #constructor
    def __init__(self, identifier, steering, speed):
        self.identifier = identifier
        self.steering = steering
        self.speed = speed

    #Input bytes
    #Error status
    def decode_pkt(self, bts): 
       dstr = bts.decode() #decoded string
       breakdown_str(self, dstr) #splits string and assigns obj

    #input: formatted string
    #output: formatted bytes
    def encode_pkt(estr):
        ret = str.encode(estr)
        return ret

    #input: current obj
    #output: formatted bytes
    def build_str(self):
        delim = '-'
        ret = str(self.identifier) + delim + str(self.steering) \
            + delim + str(self.speed)
        return ret
    
    #input: formatted string
    #ouput: int for error status, packet obj is updated
    def breakdown_str(self, fstr):
        lst = fstr.split("-")
        if(len(lst) != 3): #if three items weren't sent, something went wrong 
            return -1

        #set internal variables
        self.identifier = float(lst[0])
        self.steering = float(lst[1])
        self.speed = float(lst[2])

        #return okay
        return 0


