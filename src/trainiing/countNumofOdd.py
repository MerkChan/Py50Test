#! /usr/bin/env python
# _*_coding:utf-8_*_

'''
计算0-7组合所能构成的所有奇数。
考虑不同长度,输出所有的组合的话
需要8重遍历，不考虑。只考虑输出的组合数。
Created on 2017年6月9日
@author: duoyi
'''
def countNumofOdd(n):
#适用于n为奇数，偶数需要修改
    count_repetition =4    
    count =4
    for i in range(1,n+1):
        if i<2 :
            count_repetition *=7   
            count *=6
        else :
            count_repetition *=8  
            count *=(n+1-i)  
    return count_repetition,count   
def main():
    n=7#int(raw_input('输入一个0：9的数字n：'))
    count_repetition,count =countNumofOdd(n)
    print '奇数组合可重复总数为%d，不可重复总数为%d:' %(count_repetition,count) 
if __name__ == '__main__':
    main()

