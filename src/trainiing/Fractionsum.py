#! /usr/bin/env python
# _*_coding:utf-8_*_

'''
计算分数的和，利用python自带模块实现分数。
Created on 2017年6月9日
@author: duoyi
'''
from fractions import Fraction
def Fractionsum():
    Rsum,a,b=0,2,1    
    for i in range(1,21):
        Rsum+=Fraction(a, b)
        a,b=a+b,a
    return  Rsum   
def main():
    Rsum =Fractionsum()
    print '2/1+3/2+5/3...的前20项和为%s。' % Rsum 
if __name__ == '__main__':
    main()
