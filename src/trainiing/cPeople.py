#! /usr/bin/env python
# _*_coding:utf-8_*_
'''
CPeople类#要总结
Created on 2017年6月14日
@author: duoyi
'''

class cPeople(object):
    def __init__(self,name,age,gender,number):#构造函数
        self.name=name
        self.age=age
        self.gender=gender
        self.number=number
    def __cAlign__(self,length=0,key='l'):  #中文对齐
        slen = len(self.name)  
        if length != 0 and slen<length and key=='r':        
            if isinstance(self.name, str):  
                placeholder = ' '  
            else:  
                placeholder = u'　'    
            self.name = placeholder*(length-slen)+self.name      
    def cprint(self,length=0,key='l'):#格式化打印函数
        if 1==self.gender:
            gender=u'男'
        else:
            gender=u'女'
        self.__cAlign__(length,key)   
        print self.name+':'+'%s,%d,%d'.ljust(10) %(gender,self.age,self.number)
       
    def isgender(self,gender):#性别判定函数
        return True if gender==self.gender else False
    
def csort(Lis,keys):#根据关键字排序输出
        if '年龄'==keys:
            Lis.sort(lambda x, y: cmp(x.age, y.age), reverse=False)   
        else:
            Lis.sort(lambda x, y: cmp(x.number, y.number), reverse=False)
    
def main():
    Lis=[]
    Lis.append(cPeople(u'小明',24,1,1))
    Lis.append(cPeople(u'李小明',27,1,3))
    Lis.append(cPeople(u'玛丽书',28,0,2))
    Lis.append(cPeople(u'小萌',20,0,6))
    Lis.append(cPeople(u'小亮',18,1,7)) 
    for each in Lis:
        each.cprint(5,'r')
    print'查找'.center(30,'-')
    for each in Lis:
        if each.isgender(1):
            each.cprint()
    print'排序'.center(30,'-')
    csort(Lis, '工号')
    for each in Lis:
        each.cprint(5,'r')
if __name__ == '__main__':
    main()