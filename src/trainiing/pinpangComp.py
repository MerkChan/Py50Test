#! /usr/bin/env python
# _*_coding:utf-8_*_
'''
比赛名单
Created on 2017年6月13日
@author: duoyi
'''
import itertools
def main():
    Lis1,Lis2=['a','b','c'],['x','y','z']
    iterEntry=itertools.permutations(Lis1,3)
    for i in iterEntry:
        for j in zip(i,Lis2):
            if j in [('a','x'),('c','x'),('c','z')]:
                break
        else:
            print i, Lis2 
if __name__ == '__main__':
    main()