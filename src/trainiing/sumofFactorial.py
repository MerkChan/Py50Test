#! /usr/bin/env python
# _*_coding:utf-8_*_

'''
求和1+2！+...+20!
Created on 2017年6月8日
@author: duoyi
'''
def sumofFactorial(n):
    Rsum=0
    product=1
    for i in range(1,n+1):
        product*=i
        Rsum+=product
    return Rsum
def main():
    n=20
    print '1+2！+...+20!的和为%f' %sumofFactorial(n)
if __name__ == '__main__':
    main()