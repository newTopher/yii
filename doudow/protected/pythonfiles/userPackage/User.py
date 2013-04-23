#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import base
import pprint

class User(base.base):

    mapperInstant=None

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
        )
        self.metaData.create_all(self.engine)
        if User.mapperInstant == None :
            User.mapperInstant=base.Config.mapper(UserModel,self.userTable)

    def validUserName(self,username):
        query=self.session.query(UserModel).filter_by(username=str(username[0])).first()
        if query is not None:
            return False
        else:
            return True

    def validEmail(self,email):
        query=self.session.query(UserModel).filter_by(email=str(email[0])).first()
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
        print postData
        userModel=UserModel()
        passQuery=self.session.query(UserModel).filter_by(password=str(postData[0]['password']))
        if passQuery is not None:
            usernameList=[instant.email for instant in passQuery]
            if postData[0]['email'] in usernameList:
                emailQuery=self.session.query(UserModel).filter_by(email=str(postData[0]['email'])).first()
                if emailQuery is not None:
                    return {}






class UserModel(object):
    pass





