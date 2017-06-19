#! /usr/bin/env python
# _*_coding:utf-8_*_
'''
猴子吃桃子。
Created on 2017年6月14日
@author: duoyi
'''
def monkEpea():
    pea=1
    for i in range(1,10):
        pea=2*(pea+1)
        print 10-i,pea
    return pea


def main():
    pea=monkEpea()
    print pea
if __name__ == '__main__':
    main()