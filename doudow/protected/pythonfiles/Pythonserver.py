#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import time
import socketPackage
import sys

reload(sys)

sys.setdefaultencoding('utf8')
sys.path.append('.\\userPackage')
sys.path.append('.\\schoolPackage')
sys.path.append('.\\weiboPackage')
sys.path.append('.\\attentionlistPackage')
SERVER_LISTENING_PORT=11230
CHARSET='UTF-8'

if __name__ == "__main__":
    print '=========server start=========='
    print 'Time %s',time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
    print '==============================='

    socketStart=socketPackage.socketCreate(SERVER_LISTENING_PORT)

    print 'Listening port SERVER_LISTENING_PORT'







