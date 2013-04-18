#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

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

            dbconnectStr=self.dbType+'://'+self.dbUser+':'+self.dbPassword+'@'+self.dbHost+'/'+self.dbName+'?charset=utf8'
            self.engine=create_engine(dbconnectStr,echo=True)
            dbSession=scoped_session(sessionmaker(bind=self.engine))
            self.session=dbSession()



        def __new__(cls, dbType,dbHost,dbName,dbUser,dbPassword,dbPort):
            if dbConnect.dbSession.dbSession == None:
                obj=super(dbConnect.dbSession,cls)
                dbConnect.dbSession.dbSession=obj.__new__(cls,dbType,dbHost,dbName,dbUser,dbPassword,dbPort)
            return dbConnect.dbSession.dbSession




    def __init__(self, dbType,dbHost,dbName,dbUser,dbPassword,dbPort):
        #print dbType

        self.__dbSession=dbConnect.dbSession(dbType,dbHost,dbName,dbUser,dbPassword,dbPort).dbSession.session
        self.__dbEngine=dbConnect.dbSession(dbType,dbHost,dbName,dbUser,dbPassword,dbPort).dbSession.engine

    def __new__(cls, dbType,dbHost,dbName,dbUser,dbPassword,dbPort):
        if dbConnect.dbInstant == None:
            obj=super(dbConnect,cls)
            dbConnect.dbInstant=obj.__new__(cls, dbType,dbHost,dbName,dbUser,dbPassword,dbPort)
        return dbConnect.dbInstant

    def getDbsession(self):
        return self.__dbSession

    def getDbengine(self):
        return self.__dbEngine

