#! /usr/bin/env python
# _*_coding:utf-8_*_
'''
使用正则表达式，去除带#的注释
Created on 2017年6月13日
@author: duoyi
'''
import re
def remComments(s):
    patt= '#.+。'
    s=re.sub(patt,'',s)#非原位置操作
    return s

def main():
    sTest='2004-959-559 #这是一个国外电话号码。'
    s=remComments(sTest).strip()
    print s
if __name__ == '__main__':
    main()