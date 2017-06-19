#! /usr/bin/env python
# _*_coding:utf-8_*_
'''
将偶数分解成素数，求其中因子之差最小的一组。
Created on 2017年6月14日
@author: duoyi
'''
import math
def sumOfPrime(num):
    lis=[]
    start=2
    end=int(math.sqrt(num))+1
    for i in range(start,end+1):
        if isPrime(i) and isPrime(num-i):
            lis.append((i,num-i,abs(num-2*i)))
    lis.sort(lambda x, y: cmp(x[2], y[2]), reverse=False)
    return lis

def isPrime(n):
    if n<=1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
    
def main():
    num=int(raw_input('输入一个偶数进行分解：'))
    lis=sumOfPrime(num)  
    print lis
if __name__ == '__main__':
    main()