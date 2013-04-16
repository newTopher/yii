#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import Config

class base():

    def __init__(self):
        self.session=Config.dbsession

    def query(self):
        return self.session.execute('show tables').fetchall()
