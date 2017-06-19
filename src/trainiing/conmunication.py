#! /usr/bin/env python
# _*_coding:utf-8_*_
'''
加密通信
Created on 2017年6月13日
@author: duoyi
'''
def encode(array):
    length=len(array)
    for i in range(length):
        array[i]=(array[i]+5)%10
    array=array[::-1]
    return array
def decode(array):
    length=len(array)
    array=array[::-1]
    for i in range(length):
        array[i]=(array[i]+5)%10
    return array    
def str2IntAarry(st):
    array=[int(each) for each in st]
    return array
def IntAarry2str(array):
    st=''.join([str(each) for each in array])
    return st
def main():
    st=raw_input('输入4位数的整数通信:')
    array=str2IntAarry(st)
    codedata=encode(array)
    print IntAarry2str(codedata)
    dedata=decode(codedata)
    print IntAarry2str(dedata)
if __name__ == '__main__':
    main()