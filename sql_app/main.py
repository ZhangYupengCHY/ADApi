#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/8 0008 11:02
# @Author  : Zhang YP
# @Email   : 1579922399@qq.com
# @github  :  Aaron Ramsey
# @File    : main.py
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from sqlalchemy.ext.declarative import declarative_base
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from sql_app import models, schema,database,crud



models.Base.metadata.create_all(bind=database.db_connect.create_engine())
models.Base_kws.metadata.create_all(bind=database.db_connect.create_engine(db=database.MYSQL_KWS_DB))


# Dependencies
def get_db_team_station():
    session = database.SessionTeamStation()
    try:
        yield session
        session.commit()
    finally:
        session.close()


def get_db_kws():
    session = database.SessionKws()
    try:
        yield session
        session.commit()
    finally:
        session.close()



walmartAccountRouter = SQLAlchemyCRUDRouter(
    schema=schema.WalmartAccount,
    create_schema=schema.WalmartAccountCreate,
    db_model=models.WalmartAccount,
    db=get_db_team_station,
    delete_all_route=False,
    delete_one_route=False,
    update_route=False,
    create_route=False,
)


highQualityKwsRouter = SQLAlchemyCRUDRouter(
    schema=schema.HighQualityKeyword,
    create_schema=schema.HighQualityKeywordCreate,
    db_model=models.HighQualityKeyword,
    db=get_db_kws,
    delete_all_route=False,
    delete_one_route=False,
    update_route=False,
    create_route=False,
)


databaseRouters = APIRouter()


@databaseRouters.get('/query_kws',summary="查询共享关键词")
def query_kws(station:str=None,asin:str=None,erpsku:str=None,sku:str=None,db:Session = Depends(get_db_kws)):
    queryInfo = crud.query_high_quality_words(db=db,station=station,erpsku=erpsku,asin=asin,sku=sku)
    if isinstance(queryInfo,str):
        return {'msg':'fail','detail':queryInfo}
    return {'msg':'success','length':len(queryInfo),'data':queryInfo}




