#! /usr/bin/env python
# _*_coding:utf-8_*_

'''
列表逆序输出，可以用函数也可用切片。
Created on 2017年6月9日
@author: duoyi
'''
def listRevser(Lis):  
    Lis=Lis[::-1]
    return Lis  
def main():
    s=raw_input('请输入列表：').split(',')
    Lis =listRevser(s)
    print '逆序输出为:',Lis
if __name__ == '__main__':
    main()
