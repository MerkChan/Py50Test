#! /usr/bin/env python
# _*_coding:utf-8_*_
'''
Count the days according to the data entered
Created on 2017年6月7日
@author: duoyi
'''
import datetime
def dataCacu1(data):
    dofM=(31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    days=sum(dofM[0:(data[1]-1)])+data[2]
    if (data[0] % 4 == 0 and data[0] % 100 != 0) or data[0] % 400 == 0:
        days+=1
    return days  
def dataCacu2(data): 
    days=datetime.date(data[0],data[1],data[2])
    return days.strftime('%j')#%j 十进制表示的每年的第几天
def main():
    data=raw_input('输入日期，以冒号隔开:')
    data=data.split(':')
    data=[int(i) for i in data]
    #days1=dataCacu1(data)
    days2=int(dataCacu2(data))
    #print '%d:%d:%d is the %d-th of the %d year' %(data[0],data[1],data[2],days1,data[0])
    print '%d:%d:%d is the %d-th of the %d year' %(data[0],data[1],data[2],days2,data[0])

if __name__ == '__main__':
    main()