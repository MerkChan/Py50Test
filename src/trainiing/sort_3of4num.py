#! /usr/bin/env python
# _*_coding:utf-8_*_
'''
1,2，3,4选取3个数排序
Created on 2017年6月7日
@author: duoyi
'''

def sort_3of4num(num):
    if len(num)!=4:
        print'Error: out of the range!'
    else:
        return [(bw,sw,gw)
                for bw in num
                for sw in num
                for gw in num
                if bw != sw and bw != gw and sw != gw 
                ]
def main(num):
    result=sort_3of4num(num)
    for vari in result:
        print str(vari[0])+str(vari[1])+str(vari[2])
if __name__ == '__main__':
    num=(1,2,3,4)
    main(num)