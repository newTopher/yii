#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class dbConnect(object):

    name=123
    __dbConnect=None

    def __init__(self,dbType,dbHost,dbUser,dbPassword,dbPort):
        self.__dbType=dbType
        self.__dbHost=dbHost
        self.__dbUser=dbUser
        self.__dbPassword=dbPassword
        self.__dbPort=dbPort
        print self.__dbHost


    def __new__(cls, dbType, dbHost,dbUser,dbPassword,dbPort):
        if dbConnect.__dbConnect == None:
            cls.__dbConnect=object.__new__(cls,dbType, dbHost,dbUser,dbPassword,dbPort)
        print 123
        return cls.__dbConnect

