#!/usr/bin/env python
# coding=utf-8
# @Time    : 2018/7/6
# @Author  : zxc
# @File    : utils
# @Desc    :


import multiprocessing as mp


def cpu_num():
    """获取cpu个数"""
    return mp.cpu_count()
