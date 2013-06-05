#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import Config

class base():

    def __init__(self):
        self.session=Config.dbsession
        self.engine=Config.dbengine
        self.metaData=Config.MetaData()

    def query(self):
        pass

    def output(self,msg):
        print msg
        return str(msg)

    def formatDict(self,dict):
        for (k,v) in dict.items():
            dict[k]=str(v).encode('UTF-8')
        return dict
