#/usr/bin/python3

#class for packet structure

class packet:

    #constructor
    def __init__(self, identifier, steering, speed):
        self.identifier = identifier
        self.steering = steering
        self.speed = speed

    #getters
    def getidentifier(self, identifier):
        return self.identifier

    def getsteering(self, steering):
        return self.steering

    def getspeed(self, speed):
        return self.speed

    #setters
    def setidentifier(self, identifier):
        self.identifier = identifier

    def setsteering(self, steering):
        self.steering = steering

    def setspeed(self, speed):
        self.speed = speed



