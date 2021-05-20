#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/8 0008 9:52
# @Author  : Zhang YP
# @Email   : 1579922399@qq.com
# @github  :  Aaron Ramsey
# @File    : crud.py


from sqlalchemy.orm import Session

from sql_app import models, schema
from public_function import public_function


def get_walmart_account(db: Session, user_id: int = None, user_account: str = None):
    """
    查询walmart账号信息
    :param db:
    :type db:
    :param user_id:
    :type user_id:
    :param user_account:
    :type user_account:
    :return:
    :rtype:
    """
    if (user_id is None) and (user_account is None):
        raise TypeError('user_id 和 user_account 不能同时为空')
    if user_id is not None:
        if not public_function.is_variables_types_valid({user_id: int}):
            raise TypeError(f'user_id输入的数据类型不对.')
        return db.query(models.WalmartAccount).filter(models.WalmartAccount.id == user_id).first()
    if user_account is not None:
        if not public_function.is_variables_types_valid({user_account: str}):
            raise TypeError(f'user_account输入的数据类型不对.')
        return db.query(models.WalmartAccount).filter(models.WalmartAccount.account == user_account).first()


def get_all_walmart_accounts(db: Session, skip: int = 0, limit: int = None):
    """
    获取walmart全部账号信息
    :param db:
    :type db:
    :return:
    :rtype:
    """
    if not public_function.is_variables_types_valid({skip: int}):
        raise TypeError('skip 输入类型是整数')
    if limit is not None:
        if not public_function.is_variables_types_valid({limit: int}):
            raise TypeError('limit 输入类型是整数')
    return db.query(models.WalmartAccount).offset(skip).limit(limit).all()


def delete_walmart_account(db: Session, user_id: int = None, user_account: str = None):
    """
    删除wlamart账号
    :param db:
    :type db:
    :param user_id:
    :type user_id:
    :param user_account:
    :type user_account:
    :return:
    :rtype:
    """
    if (user_id is None) and (user_account is None):
        raise TypeError('user_id 和 user_account 不能同时为空')
    if user_id is not None:
        if not public_function.is_variables_types_valid({user_id: int}):
            raise TypeError(f'user_id输入的数据类型不对.')
        delete_walmart_account = db.query(models.WalmartAccount).filter(models.WalmartAccount.id == user_id).first()
    if user_account is not None:
        if not public_function.is_variables_types_valid({user_account: str}):
            raise TypeError(f'user_account输入的数据类型不对.')
        delete_walmart_account = db.query(models.WalmartAccount).filter(
            models.WalmartAccount.account == user_account).first()
    if delete_walmart_account:
        db.delete(delete_walmart_account)
        db.commit()
        db.flush()
        return delete_walmart_account


def update_walmart_account(db: Session, user_id: int = None, user_account: str = None):
    if (user_id is None) or (user_account is None):
        raise TypeError('user_id 和 user_account 不能为空')
    oldAccountInfo = db.query(models.WalmartAccount.account == user_account).first()
    if oldAccountInfo:
        db.commit()
        db.flush()
        db.refresh(db_item)
        return db_item


def query_high_quality_words(db:Session,station:str = None,erpsku:str = None,asin:str=None,sku:str=None,stationLimitNumber=4,queryLimit=1000):
    if not any([station,erpsku,asin,sku]):
        return 'station,erpsku,asin,sku不能同时为空'
    if len([value for value in [station,erpsku,asin,sku] if value is not None]) != 1:
        return 'station,erpsku,asin,sku同时只能查询一个'

    if station is not None:
        if ',' not in station:
            return db.query(models.HighQualityKeyword).filter(models.HighQualityKeyword.station == station).all()
        else:
            queryStations = public_function.database_query_str_2_list(station)
            if len(queryStations) > stationLimitNumber:
                return '站点查询长度不得超过4'
            queryStations  =[public_function.standardStation(station) for station in queryStations]
            return db.query(models.HighQualityKeyword).filter(models.HighQualityKeyword.station.in_(queryStations)).all()
    elif erpsku is not None:
        if ',' not in erpsku:
            return db.query(models.HighQualityKeyword).filter(models.HighQualityKeyword.erpsku == erpsku).all()
        else:
            queryErpSkuLen = public_function.database_query_str_2_list(erpsku)
            if len(queryErpSkuLen) > queryLimit:
                return f'单次erpsku查询个数不得超过{queryLimit}'
            return db.query(models.HighQualityKeyword).filter(models.HighQualityKeyword.erpsku.in_(queryErpSkuLen)).all()
    elif asin is not None:
        if ',' not in asin:
            return db.query(models.HighQualityKeyword).filter(models.HighQualityKeyword.asin == asin).all()
        else:
            queryAsinLen = public_function.database_query_str_2_list(asin)
            if len(queryAsinLen) > queryLimit:
                return f'单次asin查询个数不得超过{queryLimit}'
            return db.query(models.HighQualityKeyword).filter(models.HighQualityKeyword.asin.in_(queryAsinLen)).all()
    else:
        if ',' not in sku:
            return db.query(models.HighQualityKeyword).filter(models.HighQualityKeyword.sku == sku).all()
        else:
            querySkuLen = public_function.database_query_str_2_list(sku)
            if len(querySkuLen) > queryLimit:
                return f'单次sku查询个数不得超过{queryLimit}'
            return db.query(models.HighQualityKeyword).filter(models.HighQualityKeyword.sku.in_(querySkuLen)).all()







