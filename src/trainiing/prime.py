#! /usr/bin/env python
# _*_coding:utf-8_*_
'''
分解质因数
Created on 2017年6月8日
@author: duoyi
'''
import math
res=[]
def prime(n):
    flag=True
    start=2
    end=int(math.sqrt(n))+1
    while start<end:
        if n%start==0:
            res.append(start)
            flag=False
            prime(n/start)
            break#截至创造递归start<end，#必须执行，否则递归调用结束。将从重复上次条件，死循环。 
        else:
            start+=1
    if flag:  
        res.append(n)  
def main():
    n=int(raw_input('请输入数：'))
    prime(n)
    print res
if __name__ == '__main__':
    main()