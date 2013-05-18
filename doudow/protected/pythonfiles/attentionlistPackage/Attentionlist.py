#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import base
class Attentionlist(base.base):
    mapperInstant=None

    def __init__(self):
        base.base.__init__(self)
        self.attentionlistTable=base.Config.Table(
            'dod_attentionlist',self.metaData,
            base.Config.Column('id',base.Config.Integer,primary_key=True,autoincrement=True),
            base.Config.Column('marster_uid',base.Config.Integer),
            base.Config.Column('follower_uid',base.Config.Integer),
        )
        self.metaData.create_all(self.engine)
        if Attentionlist.mapperInstant == None :
            Attentionlist.mapperInstant=base.Config.mapper(AttentionlistModel,self.attentionlistTable)

    def getUserAttentionList(self,followerUid):
        try:
            query=self.session.query(AttentionlistModel).filter_by(follower_uid=int(followerUid[0]))
            if query is not None:
                followerList = [int(instant.marster_uid) for instant in query ]
            return followerList
        except:
            return -1


class AttentionlistModel(object):
    pass

