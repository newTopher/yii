#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import time
import socketPackage
import dbUntils
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sys.path.append('.\\userPackage')
SERVER_LISTENING_PORT=21230
CHARSET='UTF-8'

if __name__ == "__main__":
    print '=========server start=========='
    print 'Time %s',time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
    print '==============================='

    socketStart=socketPackage.socketCreate(SERVER_LISTENING_PORT)

    print 'Listening port SERVER_LISTENING_PORT'









