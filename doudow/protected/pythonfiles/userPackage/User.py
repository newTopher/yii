#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import base

class User(base.base):

    mapperInstantUser=None
    mapperInstantUserAttrInfo=None

    def __init__(self):
        base.base.__init__(self)
        self.userTable=base.Config.Table(
            'dod_user',self.metaData,
            base.Config.Column('id',base.Config.Integer,primary_key=True,autoincrement=True),
            base.Config.Column('username',base.Config.String(32)),
            base.Config.Column('name',base.Config.String(32)),
            base.Config.Column('email',base.Config.String(50),unique=True,nullable=False),
            base.Config.Column('password',base.Config.String(32),nullable=False),
            base.Config.Column('sex',base.Config.Integer,nullable=False),
            base.Config.Column('birthday',base.Config.Integer,nullable=True),
            base.Config.Column('school_id',base.Config.Integer,nullable=False),
            base.Config.Column('user_sign',base.Config.String(200)),
            base.Config.Column('details',base.Config.String(300)),
            base.Config.Column('head_img',base.Config.String(30)),
            base.Config.Column('is_active',base.Config.Integer,nullable=False),
            base.Config.Column('grate',base.Config.String(20)),
            base.Config.Column('followers_counts',base.Config.Integer,default=0),
            base.Config.Column('follow_me',base.Config.SmallInteger(4),default=0),
            base.Config.Column('attention_counts',base.Config.Integer,default=0),
        )

        self.userattrinfoTable=base.Config.Table(
            'dod_user_attrinfo',self.metaData,
            base.Config.Column('uid',base.Config.Integer,primary_key=True),
            base.Config.Column('en_name',base.Config.VARCHAR(20),nullable=True),
            base.Config.Column('constellation',base.Config.VARCHAR(20),nullable=True),
            base.Config.Column('province_id',base.Config.Integer,nullable=True),
            base.Config.Column('city_id',base.Config.Integer,nullable=True),
            base.Config.Column('location',base.Config.VARCHAR(32),nullable=True)
        )

        self.metaData.create_all(self.engine)
        if User.mapperInstantUser == None :
            User.mapperInstantUser=base.Config.mapper(UserModel,self.userTable)

        if User.mapperInstantUserAttrInfo == None :
            User.mapperInstantUserAttrInfo=base.Config.mapper(UserAttrInfoModel,self.userattrinfoTable)

    def validUserName(self,username):
        query=self.session.query(UserModel).filter_by(username=str(username[0])).first()
        self.session.flush()
        self.session.commit()
        if query is not None:
            return False
        else:
            return True

    def validEmail(self,email):
        query=self.session.query(UserModel).filter_by(email=str(email[0])).first()
        self.session.flush()
        self.session.commit()
        if query is not None:
            return False
        else:
            return True


    def userReg(self,postData):
        userModel=UserModel()
        userModel.username=postData[0]['username']
        userModel.name=postData[0]['name']
        userModel.email=postData[0]['email']
        userModel.password=postData[0]['password']
        userModel.sex=postData[0]['sex']
        userModel.birthday=postData[0]['birthday']
        userModel.school_id=postData[0]['school_id']
        userModel.user_sign=postData[0]['user_sign']
        userModel.details=postData[0]['details']
        userModel.head_img=postData[0]['head_img']
        userModel.is_active=postData[0]['is_active']
        userModel.grate=postData[0]['grate']
        try:
            self.session.add(userModel)
            self.session.flush()
            self.session.commit()
            return int(userModel.id)
        except:
            return int(0)



    def userLogin(self,postData):
        passQuery=self.session.query(UserModel).filter_by(password=str(postData[0]['password']))
        self.session.flush()
        if passQuery is not None:
            usernameList=[instant.email for instant in passQuery]
            if postData[0]['email'] in usernameList:
                emailQuery=self.session.query(UserModel).filter_by(email=str(postData[0]['email'])).first()
                if emailQuery is not None:
                    del emailQuery.__dict__['_sa_instance_state']
                    return self.formatDict(emailQuery.__dict__)
                else:
                    return -1
            else:
                return -1
        else:
            return -1


    def getUser(self,id):
        userQuery=self.session.query(UserModel,UserAttrInfoModel).filter(UserAttrInfoModel.uid==UserModel.id).filter(UserModel.id==int(id[0])).first()
        self.session.flush()
        self.session.commit()
        if userQuery is not None:
            mergeDict=dict();
            mergeDict=userQuery.UserModel.__dict__.copy()
            mergeDict.update(userQuery.UserAttrInfoModel.__dict__)
            del mergeDict['_sa_instance_state']
            mergeDict=self.formatDict(mergeDict)
            return mergeDict
        else:
            return -1

    def getUserNickName(self,id):
        query=self.session.query(UserModel).filter(UserModel.id==int(id[0])).first()
        self.session.flush()
        self.session.commit()
        if query is not None:
            return str(query.username)
        else:
            return -1

    def updateUserFollowersCounts(self,uid,tag):
            try:
                if tag==0:
                    self.session.query(UserModel).filter(UserModel.id == uid).update({'followers_counts':UserModel.followers_counts-int(1)})
                else:
                    self.session.query(UserModel).filter(UserModel.id == uid).update({'followers_counts':UserModel.followers_counts+int(1)})
                self.session.flush()
                self.session.commit()
                return True
            except:
                return False

    def updateUserAttentionCounts(self,uid,tag):
        try:
            if tag==0:
                self.session.query(UserModel).filter(UserModel.id == uid).update({'attention_counts':UserModel.attention_counts-int(1)})
            else:
                self.session.query(UserModel).filter(UserModel.id == uid).update({'attention_counts':UserModel.attention_counts+int(1)})
            self.session.flush()
            self.session.commit()
            return True
        except:
            return False



class UserModel(object):
    pass

class UserAttrInfoModel(object):
    pass




