#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Ryan'

"""
**第 0002 题:** 将 0001 题生成的 200 个激活码（或者优惠券）保存到 **MySQL** 关系型数据库中。 
"""


import uuid


def create_code(num, length):
#生成”num“个激活码，每个激活码含有”length“位
    result = []
    while True:
        uuid_id = uuid.uuid1()
        temp = str(uuid_id).replace('-', '')[:length]
        if not temp in result:
            result.append(temp)
        if len(result) == num:
            break
    return result

print create_code(200, 20)