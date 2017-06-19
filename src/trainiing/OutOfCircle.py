#! /usr/bin/env python
# _*_coding:utf-8_*_
'''
n个人围城一圈，顺序排号。从第一个开始报（1,3），报到3出局，最后留下的是？
约瑟夫环
Created on 2017年6月12日
@author: duoyi
'''
def outOfCircle(n):
    num = [i for i in range(1,n+1)]
    while len(num)>2:
        for i in num:
            pos=num.index(i)
            if (pos+1)%3==0:
                num.remove(i)
                num=num[pos:]+num[0:pos]
                break
    return num[1]
def main():
    n = int(raw_input('请输入总人数:'))
    num=outOfCircle(n)
    print num
if __name__ == '__main__':
    main()