#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import base

class School(base.base):
    mapperInstant=None

    def __init__(self):
        base.base.__init__(self)
        self.schoolTable=base.Config.Table(
            'dod_school',self.metaData,
            base.Config.Column('school_id',base.Config.SmallInteger(6),primary_key=True,autoincrement=True),
            base.Config.Column('province_id',base.Config.SmallInteger(6),unique=True),
            base.Config.Column('city_id',base.Config.SmallInteger(6)),
            base.Config.Column('school_name',base.Config.String(100),nullable=False),
            base.Config.Column('details',base.Config.String(30)),
            )
        self.metaData.create_all(self.engine)
        if School.mapperInstant == None :
            School.mapperInstant=base.Config.mapper(SchoolModel,self.schoolTable)



    def schoolList(self,cid):
        schoolQuery=self.session.query(SchoolModel).filter_by(city_id=int(cid[0]))
        if schoolQuery is not None:
            schoolList=[]
            for instant in schoolQuery:
                schoolList.append(dict(school_name=str(instant.__dict__['school_name']),school_id=instant.__dict__['school_id']))
            return schoolList
        else:
            return False








class SchoolModel(object):
    pass
