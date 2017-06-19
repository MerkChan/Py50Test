#! /usr/bin/env python
# _*_coding:utf-8_*_
'''
问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第
三个月后每个月又生一对兔子，假如兔子都不死，问第N月的兔子总数为多少？
分析：1月：1;2月：1;3月：2;4月：3;5月：5;6月：8.....
迭代过程为：f(n)=f(n-1)+f(n-2)
Created on 2017年6月8日
@author: duoyi
'''
def rabbit(n):
    if n<=2:
        return 1
    else:
        return rabbit(n-1)+rabbit(n-2)
def main():
    n=int(raw_input('请输入月数：'))
    num=rabbit(n)
    print '第%d月的兔子总数为%d。' %(n,num)
if __name__ == '__main__':
    main()