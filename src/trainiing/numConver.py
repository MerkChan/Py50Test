#! /usr/bin/env python
# _*_coding:utf-8_*_

'''
实现数转换 
Created on 2017年6月9日
@author: duoyi
'''
i=0 
Lis=[]
def decConverhex(num):
    num=int(num)
    i=0
    if num<10:
        Lis.append(str(num))
    elif 10 <= num <16:
        Lis.append(chr(num - 10 + ord('A')));
    else:
        decConverhex(num/16)
        i+=1
        num%=16
        if num<10:
            Lis.append(str(num))
        elif 10 <= num <16:
            Lis.append(chr(num - 10 + ord('A')));
    return '0x'+''.join(Lis)     
def decConveroct(num):
    num=int(num)
    i=0
    if num<8:
        Lis.append(str(num))
    else:
        decConveroct(num/8)
        i+=1
        num%=8
        if num<8:
            Lis.append(str(num))
    return '0'+''+''.join(Lis) 
def hexConverdec(num):
    s=num[2:]
    Rsum=0
    n=len(s)
    for i in range(n):
        if num<10:
            m=int(s[i])
        else :
            m=ord(s[i])-ord('A')+10
        Rsum+=m*16**(n-1-i)
    return Rsum  ####BUG
def hexConveroct(num):
    d=hexConverdec(num)
    d=decConveroct(d)####BUG
    return d
def octConverdec(num):
    s=num[1:]
    Rsum=0
    n=len(s)
    for i in range(n):
        Rsum+=int(s[i])*8**(n-1-i)
    return Rsum  
def octConverhex(num):
    d=octConverdec(num)
    print d
    d=decConverhex(d)
    return d
def main():
    Lis=[]
    s=raw_input('请输入列表：')
    #s=decConverhex(s)
    #print '0x%s'%s
    #s=decConveroct(s)
    #print '%s'%s
    #d=hexConverdec(s)
    #print '%d'%d
    d=octConverhex(s)
    print '%s'%d
if __name__ == '__main__':
    main()
