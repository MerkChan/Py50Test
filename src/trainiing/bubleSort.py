#! /usr/bin/env python
# _*_coding:utf-8_*_

'''
冒泡排序，与插入（不知道原序列顺序）
Created on 2017年6月12日
@author: duoyi
'''
def bubleSort(Lis):
    length=len(Lis)
    for i in range(length-1):
        for j in range(length-i-1):
            if Lis[j]>Lis[j+1]:
                Lis[j],Lis[j+1]=Lis[j+1],Lis[j]  
    return Lis
def insertNew(Lis,num):#二分法插入,这里偷懒
    Lis.append(num)
    if Lis[0]>Lis[-1]:
        Lis.sort(reverse=True)
    else:
        Lis.sort(reverse=False)
    return Lis.index(num),Lis
def main():
    Lis=raw_input('输入列表，以逗号隔开:').split(',')
    Lis=[int(num) for num in Lis]
    Lis=bubleSort(Lis)
    print Lis
    num=int(raw_input('输入的数字:'))
    id1,Lis=insertNew(Lis,num)
    print id1+1,Lis
if __name__ == '__main__':
    main()