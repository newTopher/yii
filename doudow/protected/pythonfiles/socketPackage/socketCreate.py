#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import socket
import process

class socketCreate():

    sockets=None

    def __init__(self,port):
        self.port=port
        self.startSocketServer()
        self.startProcess()

    def startSocketServer(self):
        try:
            sockets=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sockets.bind(('',self.port))
            sockets.listen(5)
            self.sockets=sockets
        except socket.error:
            print "socket server fair"

    def startProcess(self):
        while True:
            connection,address=self.sockets.accept()
            print "client's IP:%s, PORT:%d" % address
            try:
                requestProcess=Process()
                requestProcess.process(connection)
            except:
                pass





