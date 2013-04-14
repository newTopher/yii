#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import time
import threading
import sys

CHARSET="utf-8"

def z_decode(p):
    if p[0]=="N":                      #NULL 0x4e-'N'
        return None,p[2:]
    elif p[0]=="b":                    #bool 0x62-'b'
        if p[2] == "0":                # 0x30-'0'
            return False,p[4:]
        else:
            return True,p[4:]
    elif p[0]=="i":                    #int  0x69-'i'
        i = index(p, ";", 1)           # 0x3b-';'
        return int(p[2:i]),p[i+1:]
    elif p[0]=="d":                    #double 0x64-'d'
        i = index(p, ";", 1)           # 0x3b-';'
        return float(p[2:i]),p[i+1:]
    elif p[0]=="s":                    #string 0x73-'s'
        len_end = index(p, ":", 2)     # 0x3a-':'
        str_len = int(p[2:len_end])
        end = len_end + 1 + str_len + 2
        v = p[(len_end + 2) : (len_end + 2 + str_len)]
        return v, p[end+1:]
    elif p[0]=="a":                    #array 0x61-'a'
        list_=[]       #数组
        dict_={}       #字典
        flag=True      #类型，true-元组 false-字典
        second = index(p, ":", 2)      # 0x3a-":"
        num = int(p[2:second])  #元素数量
        pp = p[second+2:]       #所有元素
        for i in range(num):
            key,pp=z_decode(pp)  #key解析
            if (i == 0): #判断第一个元素key是否int 0
                if (not isinstance(key, int)) or (key != 0):
                    flag = False
            val,pp=z_decode(pp)  #value解析
            list_.append(val)
            dict_[key]=val
        return (list_, pp[2:]) if flag else (dict_, pp[2:])
    else:
        return p,''


def z_encode(p):
    if p == None:                               #None->PHP中的NULL
        return "N;"
    elif isinstance(p, int):                    #int->PHP整形
        return "i:%d;" % p
    elif isinstance(p, str):                    #String->PHP字符串
        p_bytes = p.encode(CHARSET);
        ret = 's:%d:"' % len(p_bytes)
        ret = ret.encode(CHARSET)
        ret = ret + p_bytes + '";'.encode(CHARSET)
        ret = str(ret)
        return ret
    elif isinstance(p, bool):                   #boolean->PHP布尔
        b=1 if p else 0
        return 'b:%d;' % b
    elif isinstance(p, float):                  #float->PHP浮点
        return 'd:%r;' % p
    elif isinstance(p, list) or isinstance(p, tuple):        #list,tuple->PHP数组(下标int)
        s=''
        for pos,i in enumerate(p):
            s+=z_encode(pos)
            s+=z_encode(i)
        return "a:%d:{%s}" % (len(p),s)
    elif isinstance(p, dict):                   #字典->PHP数组(下标str)
        s=''
        for key in p:
            s+=z_encode(key)
            s+=z_encode(p[key])
        return "a:%d:{%s}" % (len(p),s)
    else:                                       #其余->PHP中的NULL
        return "N;"


def index(str,sign,pos=0):
    for i in range(len(str)):
        if i<=pos:
            continue
        if str[i]==sign:
            return i
            break
    else:
        return -1




class Process(threading.Thread):

    def __init__(self,socket):
        threading.Thread.__init__(self)
        self.compileDirct={}
        self.REQUEST_MIN_LEN=10
        self.TIME_OUT=180
        self._socket=socket

    def run(self):
        try:
            firstBuffer=self._socket.recv(16*1024)
            if len(firstBuffer)<self.REQUEST_MIN_LEN:
                print ("非法包，小于最小长度: %s" % firstBuffer)
                self._socket.close()
                return
            firstComma=index(firstBuffer,',')
            totalLen=int(firstBuffer[0:firstComma])
            print "message length is %d" % totalLen

            reqMsg = firstBuffer[firstComma+1:]
            while (len(reqMsg) < totalLen):
                reqMsg = reqMsg + self._socket.recv(16 * 1024)    #确保接收完全
            moudleName,methodName,params=self.__parsePythonMoudle(reqMsg)

            if moudleName not in self.compileDirct:
                try:
                    callMoudle=__import__(moudleName)
                    self.compileDirct['moudleName']=callMoudle
                except Exception as e:
                    print ('模块不存在:%s' % moudleName)
                    self._socket.sendall(("F" + "module '%s' is not exist!" % moudleName).encode(CHARSET))
                    self.__close()
                    return
            else:
                callMoudle=self.compileDirct['moudleName']




            try:
                className=getattr(callMoudle,moudleName)
                obj=className()
                useMethod=getattr(obj,methodName)
            except TypeError as e:
                print ('函数不存在:%s' % methodName)
                self._socket.sendall(("F" + "function '%s()' is not exist!" % methodName).encode(CHARSET)) #异常
                self.__close()
                return


            try:
                params = '['+','.join([repr(x) for x in params])+']'
                responseResult=useMethod(eval(params))
            except Exception as e:
                print ('调用Python业务函数异常', e )
                errType, errMsg, traceback = sys.exc_info()
                self._socket.sendall(("F%s" % errMsg).encode(CHARSET)) #异常信息返回
                self.__close()
                return


            try:
                responseStr = z_encode(responseResult)
                responseStr = "S" + responseStr
                #print ("返回包：%s" % rspStr)
                self._socket.sendall(responseStr.encode(CHARSET))
            except Exception as e:
                print ('发送消息异常', e)
                errType, errMsg, traceback = sys.exc_info()
                self._socket.sendall(("F%s" % errMsg).encode(CHARSET)) #异常信息返回



            finally:
                self.__close()
            return












        except TypeError:
            #print "recive msg error %s" % e
            self.__close()
            return



    def __parsePythonMoudle(self,reqMsg):
        v,p=z_decode(reqMsg);
        params=v
        pythonMoudle=params[0]
        pos=pythonMoudle.find("::")
        moudleName=pythonMoudle[:pos]
        methodName=pythonMoudle[pos+2:]
        return moudleName,methodName,params[1:]




    def __close(self):
        self._socket.close()






