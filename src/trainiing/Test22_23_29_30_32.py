#! /usr/bin/env python
# _*_coding:utf-8_*_

'''
22题目 Outofn_th:输入整数V，输出其m-n位
23题目 ChangeForLis:输入列表，最大与第一个交换，最小与最后交换
29题目 python字符串有自带的string.count()方法
30题目 countFreq:输入中文字符串统计出现次数最多的3个中文字
32题目 python自带的sort与sorted方法带reversed参数即可实现，也可以用自己编写的bubleSort实现。
Created on 2017年6月12日
@author: duoyi
'''

def Outofn_th(num,n,m):
    num=str(num)
    return int(num[n-1:m])
def ChangeForLis(Lis):
    Lis[0],Lis[-1]=max(Lis),min(Lis)
    return Lis
def countFreq(inputStr):
    dic={}
    for i in range(len(inputStr)):
        num=inputStr.count(inputStr[i])
        if inputStr[i] not in dic:
            dic[inputStr[i]]=num
        elif num>dic[inputStr[i]]:
            dic[inputStr[i]]=num
    return dic
def countThird(inputStr):
    dic=countFreq(inputStr)
    lis=sorted(dic.iteritems(), lambda x, y: cmp(x[1], y[1]), reverse = True)#key=lambda d:d[1]等效
    return lis   
def main():
    '''num=int(raw_input('输入整数:'))
    buffer=raw_input('输入输出的位数m,n:').split(',')
    n,m=(int(each) for each in buffer)
    Res=Outofn_th(num,n,m)
    print Res
    Lis=[35,2,4,78,1,55,255,43]
    num=ChangeForLis( Lis)
    print  Lis'''
    inputStr=unicode(raw_input('输入一串中文:'),'utf-8')#raw_input的返回值是str类型，非unicode类型，与文本的用的编码类型无关。
    lis=countThird(inputStr)
    for key in lis:
        print key[0], key[1]
if __name__ == '__main__':
    main()