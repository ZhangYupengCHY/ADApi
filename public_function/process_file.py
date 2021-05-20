#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/7 0007 10:01
# @Author  : Zhang YP
# @Email   : 1579922399@qq.com
# @github  :  Aaron Ramsey
# @File    : process_file.py

"""
处理文件相关的
"""


import os


def is_file(filePath):
    # 是否是有效的文件路径
    return os.path.exists(filePath)



