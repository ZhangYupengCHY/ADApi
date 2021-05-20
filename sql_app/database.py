#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/7 0007 16:41
# @Author  : Zhang YP
# @Email   : 1579922399@qq.com
# @github  :  Aaron Ramsey
# @File    : database.py


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sql_app.models import Base,Base_kws


MYSQL_SERVER = 'wuhan.yibai-it.com'
MYSQL_USER = 'marmot'
MYSQL_PASSWORD = 'marmot123'
MYSQL_PORT = 33061
MYSQL_DB = 'team_station'
MYSQL_KWS_DB = "server_camp_report"


class db_connect:

    @staticmethod
    def create_engine(server=MYSQL_SERVER,user=MYSQL_USER,password=MYSQL_PASSWORD,port=MYSQL_PORT,db=MYSQL_DB,charset='utf8'):
        url: str = f'mysql+pymysql://{user}:{password}@{server}:{port}/{db}?charset={charset}'
        return create_engine(url, pool_pre_ping=True)


# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind={Base:db_connect.create_engine(db=MYSQL_DB),Base_kws:db_connect.create_engine(db=MYSQL_KWS_DB)})
SessionTeamStation = sessionmaker(autocommit=False, autoflush=False, bind=db_connect.create_engine(db=MYSQL_DB))
SessionKws = sessionmaker(autocommit=False, autoflush=False, bind=db_connect.create_engine(db=MYSQL_KWS_DB))



