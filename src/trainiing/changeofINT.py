#! /usr/bin/env python
# _*_coding:utf-8_*_

'''
请输入一个不多于5位的整数，求长度，逆序输出。
Created on 2017年6月9日
@author: duoyi
'''
def changeofINT(n):
    n=str(n)
    m=len(n)
    n=int(n[::-1])#步长>0 切片操作从左往右进行;步长<0 切片操作从右往左进行
    if m >= 5:
        print '超出输出范围！'
        return None
    return m,n
def main():
    while True:
        n=int(raw_input('请输入一个不多于5位的整数：'))
        length,revsr=changeofINT(n)
        if length>0:
            break
    print '输入的整数长度为%d,逆序输出为%d' %(length,revsr)
if __name__ == '__main__':
    main()
