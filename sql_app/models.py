#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/7 0007 16:53
# @Author  : Zhang YP
# @Email   : 1579922399@qq.com
# @github  :  Aaron Ramsey
# @File    : models.py

"""
模型设计
"""

from sqlalchemy import Column, Integer, String, DateTime,Text,Float
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
Base_kws = declarative_base()


class WalmartAccount(Base):
    """
    walmart全部的账号信息
    """
    __tablename__ = 'walmart_account'
    id = Column(Integer, primary_key=True, nullable=True)
    account = Column(String, nullable=False)
    updatetime = Column(DateTime, nullable=False)


class HighQualityKeyword(Base_kws):
    __tablename__ = 'high_quality_keywords'

    id = Column(BIGINT(20), primary_key=True)
    station = Column(String(128, 'utf8_unicode_ci'))
    erpsku = Column(String(255, 'utf8_unicode_ci'))
    asin = Column(String(128, 'utf8_unicode_ci'))
    sku = Column(String(128, 'utf8_unicode_ci'))
    campaign_name = Column(Text(collation='utf8_unicode_ci'))
    ad_group_name = Column(Text(collation='utf8_unicode_ci'))
    match_type = Column(Text(collation='utf8_unicode_ci'))
    customer_search_term = Column(Text(collation='utf8_unicode_ci'))
    impression = Column(BIGINT(20))
    click = Column(BIGINT(20))
    spend = Column(Float(asdecimal=True))
    sale = Column(Float(asdecimal=True))
    order = Column(BIGINT(20))
    ctr = Column(Text(collation='utf8_unicode_ci'))
    cpc = Column(Float(asdecimal=True))
    acos = Column(Text(collation='utf8_unicode_ci'))
    cr = Column(Text(collation='utf8_unicode_ci'))
    sku_sale = Column(Float(asdecimal=True))
    item_name = Column(Text(collation='utf8_unicode_ci'))
    kws_lang = Column(String(20, 'utf8_unicode_ci'))
    updatetime = Column(DateTime)
    keyword_1 = Column(String(128, 'utf8_unicode_ci'))
    keyword_2 = Column(String(128, 'utf8_unicode_ci'))
    keyword_3 = Column(String(128, 'utf8_unicode_ci'))
    keyword_4 = Column(String(128, 'utf8_unicode_ci'))
    keyword_5 = Column(String(128, 'utf8_unicode_ci'))
    keyword_6 = Column(String(128, 'utf8_unicode_ci'))
    keyword_7 = Column(String(128, 'utf8_unicode_ci'))
    keyword_8 = Column(String(128, 'utf8_unicode_ci'))
    keyword_9 = Column(String(128, 'utf8_unicode_ci'))
    keyword_10 = Column(String(128, 'utf8_unicode_ci'))