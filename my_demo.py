#! /usr/bin/env python2.7
# encoding=utf8
"""
单测Demo
author: evilcapricorn0110@gmail.com
date: 2018-03
"""

from pprint import pprint

class MyDemoError(Exception):
    def __init__(self, message):
        super(MyDemoError, self).__init__(message)
        self.value = "MyDemoError: {0}".format(message)


class MyDemo(object):
    def __init__(self):
        pass
    
    def func1(self, sex, age):
        if '男' == sex and age > 18:
            return '看av'
            
        if '女' == sex and age > 18:
            return '逛taobao'
                
    def func2(self, day):
        if day >=1 and day <= 5:
            return '上班'
        if 6 == day or 7 == day:
            return '加班'
        raise MyDemoError('统一2月30日，31日放假，或者星期八休息')
    
    def func3(self, x, y):
        return x / y


def my_function(self, x, y):
    pprint.pprint('a')
    return x + y