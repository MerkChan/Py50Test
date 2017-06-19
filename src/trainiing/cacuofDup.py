#! /usr/bin/env python
# _*_coding:utf-8_*_

'''
根据a,n，求和s=a+aa+aaa+...
Created on 2017年6月8日
@author: duoyi
'''
def cacuofDup(a,n):
    Rsum=0
    for i in range(n):
        Rsum+=a*(n-i)*10**i
    return Rsum
def main():
    s=raw_input('请输入重复的数字a及次数n：').split(',')
    a,n=int(s[0]),int(s[1])
    Rsum=cacuofDup(a,n)
    print '根据%d,%d,求和s=a+aa+aaa+...的结果为：%d' %(a,n,Rsum)
if __name__ == '__main__':
    main()