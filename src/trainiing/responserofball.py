#! /usr/bin/env python
# _*_coding:utf-8_*_

'''
小球从100米下落，每次弹起的高度为原来一半，求第N次
落地时经过的路程与下一次弹起高度。
Created on 2017年6月8日
@author: duoyi
'''
def ball(n):
    intial=100.0
    endHight=intial/(2**n)
    Rsum=100
    for i in range(n):
        Rsum+=2*intial/(2**(i+1))
    return Rsum,endHight
def main():
    n=int(raw_input('请输入次数n：'))
    Res=ball(n)
    print '第%d次落地时经过的路程为%f与下一次弹起高度为%f' %(n,Res[0],Res[1])
if __name__ == '__main__':
    main()