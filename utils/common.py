#!/usr/bin/env python
# coding=utf-8
# @Time    : 2018/7/6
# @Author  : zxc
# @File    : utils
# @Desc    :

import math
from datetime import datetime, timedelta, date
import time
import requests
import json
import re
import random


def format_html_str(strs, has_text=True):
    """获取html内容"""
    new_str = ''
    if strs and has_text:
        new_str = strs.text.strip()
    elif strs:
        new_str = strs.strip()
    return new_str


def random_str(length=8):
    """随机字符串生成"""
    init_str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    for i in range(length):
        init_str += chars[random.randint(0, length)]
    return init_str


def trim_str(text):
    """去除字符串空格"""
    if text is None:
        text = ""
    if isinstance(text, str):
        text = text.strip().lower()
    return text


def int_length(number):
    """求整数的长度"""
    return len(str(number))


def fetch_location_amap(id_, address):
    """根据地址获取经纬度"""
    result = {'location': None}
    try:
        url = 'https://restapi.amap.com/v3/geocode/geo?output=JSON&key={key}&address={address}'
        rsp = requests.get(url.format(key=cls.KEY, address=address))
        if rsp.status_code == 200:
            text = json.loads(rsp.text)
            if text['status'] == '1':
                return text['geocodes'][0]
            else:
                return result
        else:
            return result
    except Exception as e:
        print('cid==>', id_, "fetch error::::", e, ":::")
    return result


def fetch_business_area(points):
    """获取经纬度所在的商圈"""
    result = ("", "")
    try:
        url = 'https://restapi.amap.com/v3/geocode/regeo?output=JSON&key={key}&radius=1000&extensions=base&batch=false&roadlevel=0&location={points}'
        rsp = requests.get(url.format(key=cls.KEY, points=points))
        if rsp.status_code == 200:
            text = json.loads(rsp.text)
            if text['status'] == '1':
                add = text['regeocode']['addressComponent']
                building = add['building']['type'] if add['building']['type'] else ''
                bus_area = [row['name'] for row in add['businessAreas']]
                bus_area = ",".join(bus_area)
                return bus_area, building
            else:
                return result
        else:
            return result
    except Exception as e:
        print('points ==>', points, "ERRORS  ::::", e, ":::")
    return result


def format_time():
    """格式化时间"""
    pass


def call_dingding(content: str, mobiles=['18210275388']) -> None:
    """钉钉通知服务
    """
    try:
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        data = {
            "msgtype": "text",
            "text": {
                "content": f'douban_spider报警:{content}'
            },
            "at": {
                "atMobiles": mobiles,
                "isAtAll": False
            }
        }
        url = 'https://oapi.dingtalk.com/robot/send?access_token=039cb5d1843ff2668b7d3685b20a0b9b11df2257304d2f2c477a2291f36a74c2'
        requests.post(url=url, headers=headers, data=json.dumps(data))
    except Exception as e:
        print(str(e))


def str2date(s):
    return datetime(*time.strptime(s, '%Y-%m-%d')[:6])


def date2str(d):
    if isinstance(d, (datetime, date)):
        return d.strftime('%Y-%m-%d')

    return d


def get_prev_date(d, days=1):
    return d - timedelta(days=days)


def get_next_date(d, days=1):
    return d + timedelta(days=days)


def datetime2str(d):
    if isinstance(d, datetime):
        return d.strftime('%Y-%m-%d %H:%M:%S')

    return d


def str2datetime(s):
    return datetime(*time.strptime(s, '%Y-%m-%d %H:%M:%S')[:6])


def time_delta_minutes(d1, d2):
    if d1 > d2:
        delta = d1 - d2
    else:
        delta = d2 - d1
    return math.ceil(delta.seconds / 60)


def get_the_weekday_of_date(d, weekday=6):
    """ 获取给定日期的周内指定星期数的日期，默认获取星期天
    参数
        date: 日期，datetime.date或datetime.datetime类型
        weekday: 周几,0-6 周一到周日
    """
    if isinstance(d, (datetime, date)):
        return d + timedelta(days=weekday-d.weekday())


def ranking(values_list, key, reverse=False, rank_field='rank'):
    """ 排序
    参数
        values_list,值列表
        key,排序
        reverse,是否逆序,True 是 False否
    """
    i = 1
    for v in sorted(values_list, key=key, reverse=reverse):
        v[rank_field] = i


if __name__ == '__main__':
    d2 = get_the_weekday_of_date(str2date('2019-09-28'), 0)
    d3 = get_the_weekday_of_date(str2date('2019-09-28'), 6)
    d4 = get_the_weekday_of_date(str2date('2019-09-28'), 5)
    str2date('1985-11-31')
    # d = str2date('2019-09-02') - str2date('2019-09-01')
    print(d2, d3, d4)
