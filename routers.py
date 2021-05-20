#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/6 0006 17:35
# @Author  : Zhang YP
# @Email   : 1579922399@qq.com
# @github  :  Aaron Ramsey
# @File    : main.py

from fastapi import FastAPI, UploadFile, File, Body,APIRouter,HTTPException
from starlette.responses import FileResponse, StreamingResponse


import static
import schema
from public_function import accessManager
from loguru import logger

router = APIRouter()


@router.get('/')
def home():
    logger.info('visit homepage.')
    return 'WELCOME TO ADapi'


@router.post("/download_station_folder", summary="download station file")
async def download_station_folder(token: str, station: schema.stationRequest):
    # 处理下载文件
    if token != static.TOKEN:
        raise HTTPException(status_code=404, detail="INVALID TOKEN")
    # 处理逻辑
    path = r"C:\Users\Administrator\Desktop\zouminy_de.zip"
    return FileResponse(path)


@router.post("/upload_station_folder", summary="Upload station file")
async def upload_station_folder(token: str,  upload_file: UploadFile = File(...)):
    # 处理上传文件
    if token != static.TOKEN:
        raise HTTPException(status_code=404, detail="TOKEN ERROR")
    # # 处理逻辑
    # savePath = r"C:\Users\Administrator\Desktop\smandy_es2.zip"
    # with open(savePath, 'wb+') as f:
    #     f.write(file.file.read())  # async write
    return {'token': token,'file':upload_file.filename}


@router.get('/getToken')
def get_token(iss: str, secret: str):
    # 获取token
    requestCode = iss + secret
    token = accessManager.hash_code(requestCode)
    return {'token': token}