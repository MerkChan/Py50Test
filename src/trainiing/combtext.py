#! /usr/bin/env python
# _*_coding:utf-8_*_

'''
合并文件A和B中的字符串，以字母升序排列，写入文件C。
Created on 2017年6月12日
@author: duoyi
'''
def combtext():
    try:
        AObj=open('A.txt','r')
        BObj=open('B.txt','r')
        st=AObj.read().replace('\n','' )+BObj.read().replace('\n','' )
        AObj.close()
        BObj.close()
        #std=list(st)
        #std.sort()
        std=sorted(st,lambda x, y: cmp(x, y))#等效于上面两条句子
        st=''.join(std)
        CObj=open('C.txt','a')
        CObj.write(st)
        CObj.close()
    except IOError,e:
        print 'file open error:',e
def main():
    combtext()
if __name__ == '__main__':
    main()
