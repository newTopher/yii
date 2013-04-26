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
                weiboBackData=list()
                weiboBackData.append(int(weiboModel.w_id))
                weiboBackData.append(int(weiboModel.create_time))
                weiboBackData.append(str(weiboModel.text))
                weiboBackData.append(int(weiboModel.reposts_counts))
                weiboBackData.append(int(weiboModel.comments_counts))
                weiboBackData.append(str(weiboModel.pics))
                weiboBackData.append(str(weiboModel.other_attr))
                weiboBackData.append(str(weiboModel.source))

                return weiboBackData
            except:
                return -2
        except:
            return -1


class WeiboModel(object):
    pass
