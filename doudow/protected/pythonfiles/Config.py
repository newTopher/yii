import dbUntils
from sqlalchemy.orm import mapper
from datetime import datetime
from sqlalchemy import *

dbconn=dbUntils.dbConnect.dbConnect('mysql+mysqldb','db4free.net','doudow','doudow','doudow','3306')
dbsession=dbconn.getDbsession()
dbengine=dbconn.getDbengine()
