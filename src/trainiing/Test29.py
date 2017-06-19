#! /usr/bin/env python
# _*_coding:utf-8_*_
'''
函数引用
Created on 2017年6月13日
@author: duoyi
'''
def fun(x):
    return lambda y:range(1,x+y)
def fun2(x,y):
    y=range(1,x+y)
    return y
def main():
    a=fun(2)
    b=fun2
    print a(3)
    print b(2,3)

if __name__ == '__main__':
    main()