#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import base

class User(base.base):

    mapperInstant=None

    def __init__(self):
        base.base.__init__(self)
        self.userTable=base.Config.Table(
            'dod_user',self.metaData,
            base.Config.Column('id',base.Config.Integer,primary_key=True),
            base.Config.Column('username',base.Config.Unicode(32)),
            base.Config.Column('name',base.Config.Unicode(32)),
            base.Config.Column('email',base.Config.Unicode(50),unique=True,nullable=False),
            base.Config.Column('password',base.Config.Unicode(32),nullable=False),
            base.Config.Column('sex',base.Config.Integer,nullable=False),
            base.Config.Column('birthday',base.Config.Integer,nullable=True),
            base.Config.Column('school_id',base.Config.Integer,nullable=False),
            base.Config.Column('user_sign',base.Config.Unicode(200)),
            base.Config.Column('details',base.Config.Unicode(300)),
            base.Config.Column('head_img',base.Config.Unicode(30)),
            base.Config.Column('is_active',base.Config.Integer,nullable=False),
            base.Config.Column('grate',base.Config.Unicode(20)),
        )
        self.metaData.create_all(self.engine)
        if User.mapperInstant == None :
            User.mapperInstant=base.Config.mapper(UserModel,self.userTable)

    def validUserName(self,id):
        for instant in self.session.query(UserModel).filter_by(id=id[0]):
            print instant.username
            return instant.username



class UserModel(object):
    pass





