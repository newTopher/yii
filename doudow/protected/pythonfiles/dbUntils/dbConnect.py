#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class dbConnect(object):

    dbInstant=None

    class dbSession(object):
        dbSession=None

        def __init__(self,dbType,dbHost,dbName,dbUser,dbPassword,dbPort):
            self.dbType=dbType
            self.dbHost=dbHost
            self.dbName=dbName
            self.dbUser=dbUser
            self.dbPassword=dbPassword
            self.dbPort=dbPort



        def __new__(cls, dbType,dbHost,dbName,dbUser,dbPassword,dbPort):
            if dbConnect.dbSession.dbSession == None:
                obj=super(dbConnect.dbSession,cls)
                dbConnect.dbSession.dbSession=obj.__new__(cls,dbType,dbHost,dbName,dbUser,dbPassword,dbPort)
            return dbConnect.dbSession.dbSession




    def __init__(self, dbType,dbHost,dbName,dbUser,dbPassword,dbPort):
        #print dbType

        self.dbSession=dbConnect.dbSession.dbSession(dbType,dbHost,dbName,dbUser,dbPassword,dbPort)

    def __new__(cls, dbType,dbHost,dbName,dbUser,dbPassword,dbPort):
        if dbConnect.dbInstant == None:
            obj=super(dbConnect,cls)
            dbConnect.dbInstant=obj.__new__(cls, dbType,dbHost,dbName,dbUser,dbPassword,dbPort)
        return dbConnect.dbInstant

