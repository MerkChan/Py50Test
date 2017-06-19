#! /usr/bin/env python
# _*_coding:utf-8_*_
'''
checkerboard
Created on 2017年6月8日
@author: duoyi
'''
def checkerboard():
    for i in range(8):
        for j in range(8):
            if(i + j) % 2 == 0:
                print '%c' %219,
            else:
                print '%c' %1,
        print''
def main():
    checkerboard()
if __name__ == '__main__':
    print '*'*5+'checkerboard'+'*'*5
    main()
    print '*'*9+'end'+'*'*10