#! /usr/bin/env python
# _*_coding:utf-8_*
'''
28题目
Created on 2017年6月14日
Simboard
@author: duoyi
'''
import itertools
import string
Aphals,Num=string.letters[26:],string.digits

def Simboard(key='left'):
    naturels=itertools.count(1)
    left=0
    right=0
    count=0
    for i in naturels:
        if count<=100:
            if 0==i%2:
                if 0==i%5:
                    count+=1
                    if 'left'==key:
                        print count,
                        print '%d,left:%s'%(i,Aphals[left])
                        i+=1
                        count+=1
                        print count,
                        print '%d,right:%d'%(i,int(Num[right]))
                    else:
                        print count,
                        print '%d,right:%d'%(i,int(Num[right]))
                        i+=1
                        count+=1
                        print count,
                        print '%d,left:%s'%(i,Aphals[left])
                    left,right=(left+1)%26,(right+1)%10
                else:
                    count+=1
                    print count,
                    print '%d,left:%s'%(i,Aphals[left])
                    left=(left+1)%26
            elif 0==i%5:
                count+=1
                print count,
                print '%d,right:%d'%(i,int(Num[right]))
                right=(right+1)%10
            
            
if __name__ == '__main__':
    Simboard('rignt')