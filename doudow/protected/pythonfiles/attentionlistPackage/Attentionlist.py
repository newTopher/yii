#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import base
import userPackage
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

    def cancelAttention(self,uids):
        try:
            self.session.query(AttentionlistModel).filter(AttentionlistModel.marster_uid==int(uids[0]['muid']),AttentionlistModel.follower_uid==int(uids[0]['fuid'])).delete()
            self.session.commit()
            self.session.flush()
            userModel=userPackage.User()
            userModel.updateUserFollowersCounts(int(uids[0]['muid']),0)
            userModel.updateUserAttentionCounts(int(uids[0]['fuid']),0)
            return True
        except:
            return False

    def addAttention(self,uids):
        attentionModel=AttentionlistModel()
        attentionModel.marster_uid=int(uids[0]['muid'])
        attentionModel.follower_uid=int(uids[0]['fuid'])
        try:
            self.session.add(attentionModel)
            self.session.commit()
            self.session.flush()
            userModel=userPackage.User()
            userModel.updateUserFollowersCounts(int(uids[0]['muid']),1)
            userModel.updateUserAttentionCounts(int(uids[0]['fuid']),1)
            return True
        except:
            return False

    def showFollowers(self,muid):
        listquery=self.session.query(AttentionlistModel.follower_uid).filter(AttentionlistModel.marster_uid==int(muid[0]))
        self.session.commit()
        self.session.flush()
        if listquery is not None:
            followerList=list()
            for instant in listquery:
                followerList.append(int(instant.follower_uid))
            userModel=userPackage.User()
            return userModel.getUserNameByUidlist(tuple(followerList))
        else:
            return False

    def showAttentions(self,fuid):
        listquery=self.session.query(AttentionlistModel.marster_uid).filter(AttentionlistModel.follower_uid==int(fuid[0]))
        self.session.commit()
        self.session.flush()
        if listquery is not None:
            attentionList=list()
            for instant in listquery:
                attentionList.append(int(instant.marster_uid))
            userModel=userPackage.User()
            return userModel.getUserNameByUidlist(tuple(attentionList))
        else:
            return False

        


class AttentionlistModel(object):
    pass

