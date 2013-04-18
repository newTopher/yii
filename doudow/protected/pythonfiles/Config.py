import dbUntils
from sqlalchemy.orm import mapper
from datetime import datetime
from sqlalchemy import *

dbconn=dbUntils.dbConnect.dbConnect('mysql+mysqldb','localhost','doudow','root','root','3306')
dbsession=dbconn.getDbsession()
dbengine=dbconn.getDbengine()
