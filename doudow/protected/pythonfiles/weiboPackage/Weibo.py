#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import base

class Weibo(base.base):
    mapperInstant=None

    def __init__(self):
        base.base.__init__(self)
        self.weiboTable=base.Config.Table(
            'dod_weibo',self.metaData,
            base.Config.Column('w_id',base.Config.Integer,primary_key=True,autoincrement=True),
            base.Config.Column('uid',base.Config.Integer),
            base.Config.Column('create_time',base.Config.Integer),
            base.Config.Column('text',base.Config.VARCHAR(140),nullable=False),
            base.Config.Column('reposts_counts',base.Config.Integer,default=0),
            base.Config.Column('comments_counts',base.Config.Integer,default=0),
            base.Config.Column('pics',base.Config.VARCHAR(250),nullable=True),
            base.Config.Column('other_attr',base.Config.VARCHAR(250),nullable=True),
            base.Config.Column('source',base.Config.VARCHAR(32),nullable=True),
            base.Config.Column('retweeted_status',base.Config.VARCHAR(140),default=None)
            )
        self.metaData.create_all(self.engine)
        if Weibo.mapperInstant == None :
            Weibo.mapperInstant=base.Config.mapper(WeiboModel,self.weiboTable)

    def publishNewWeibo(self,postData):
        weiboModel=WeiboModel()
        weiboModel.uid=int(postData[0]['uid'])
        weiboModel.text=str(postData[0]['text'])
        weiboModel.pics=str(postData[0]['pics'])
        weiboModel.create_time=int(postData[0]['create_time'])
        weiboModel.other_attr=str(postData[0]['other_attr'])
        weiboModel.source=str(postData[0]['source'])

        try:
            self.session.add(weiboModel)
            self.session.flush()
            self.session.commit()

            try:
                weiboBackData=dict()
                weiboBackData['w_id']=int(weiboModel.w_id)
                weiboBackData['uid']=int(weiboModel.uid)
                weiboBackData['create_time']=int(weiboModel.create_time)
                weiboBackData['text']=str(weiboModel.text)
                weiboBackData['reposts_counts']=int(weiboModel.reposts_counts)
                weiboBackData['comments_counts']=int(weiboModel.comments_counts);
                weiboBackData['pics']=str(weiboModel.pics)
                weiboBackData['other_attr']=str(weiboModel.other_attr)
                weiboBackData['source']=str(weiboModel.source)

                return weiboBackData
            except:
                return -2
        except:
            return -1


    def repostWeibo(self,postData):
        weiboModel=WeiboModel()
        weiboModel.uid=int(postData[0]['uid'])
        weiboModel.text=str(postData[0]['text'])
        weiboModel.retweeted_status=int(postData[0]['w_id']);
        weiboModel.create_time=int(postData[0]['create_time'])
        weiboModel.source=str(postData[0]['source'])

        try:
            self.session.add(weiboModel)
            self.session.flush()
            self.session.commit()

            try:
                weiboBackData=dict()
                weiboBackData['w_id']=int(weiboModel.w_id)
                weiboBackData['uid']=int(weiboModel.uid)
                weiboBackData['create_time']=int(weiboModel.create_time)
                weiboBackData['text']=str(weiboModel.text)
                weiboBackData['source']=str(weiboModel.source)

                return weiboBackData
            except:
                return -2
        except:
            return -1

    def destroyWeibo(self,wid):
        try:
            self.session.query(WeiboModel).filter(WeiboModel.w_id==int(wid[0])).delete()
            self.session.flush()
            return True
        except:
            return False

    def getCurrNewWeiboList(self,postData):
        try:
            query=self.session.query(WeiboModel).filter(WeiboModel.uid.in_(postData[0]['attentionUserList'])).order_by('create_time DESC').offset(0).limit(50)
            if query is not None:
                #weiboList=[[int(instant.w_id),int(instant.uid),int(instant.reposts_counts),int(instant.comments_counts),str(instant.text),int(instant.create_time),str(instant.pics),str(instant.other_attr),str(instant.source)] for instant in query]
                weiboList=list()
                for instant in query:
                    del instant.__dict__['_sa_instance_state']
                    weiboList.append(self.formatDict(instant.__dict__))
                return weiboList
        except:
            return -1









class WeiboModel(object):
    pass
