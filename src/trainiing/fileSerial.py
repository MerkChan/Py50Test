#!/usr/bin/python
#coding=utf-8
'''
读取一个文件将其序列化 fileSerial
Created on 2017年6月12日
@author: duoyi
'''
import marshal
dAccount_info={"12232":["sss",123,456],"23334":["ttt",234,456]}
pFile=file('accout.txt','wb')
marshal.dump(dAccount_info, pFile)
pFile.close()
 
 
pFile=file('accout.txt','rb')
d=marshal.load(pFile)
print d
pFile.close()