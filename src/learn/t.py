#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
#subtoal=0
#for i in range(5):
#    subtoal+=int(raw_input('Enter a number:'))
#print subtoal
#a=(int(raw_input('Enter a number:')) for i in range(5))
#print a
#print sum(int(raw_input('Enter a number:')) for i in range(5))
def fun(x):
    return lambda y:range(1,x+y)
def fun2(x,y):
    y=range(1,x+y)
    return y
a=fun(2)
b=fun2
print a(3)
print b(2,3)
def CreateGenerator():
    for i in range(3):
        yield i*i
for i in CreateGenerator():
    print i,',',
'''

def is_chinese(uchar):
    """判断一个unicode是否是汉字"""
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False
 
def fill_text_to_print_width(text, width):
    stext = str(text)
    utext = stext.decode("utf-8")
    cn_count = 0
    for u in utext:
        if is_chinese(u):
            cn_count += 1
    return " " * (width - cn_count - len(utext)) + stext
 
 
def main():      
    s='''师门任务20次,0,80
除魔任务20次,0,100
闹事妖怪10次,0,50
运镖任务5次,0,40
挖宝5次,0,40
角色升级1次,0,50
完成4次江湖悬赏令,10,40
任务链整摆环30次,0,90
野外暗雷战斗60次,0,50
获得修炼经验400点,0,50
'''
    lis=s.strip().replace('\n',',').split(',')
    length=len(lis)
    lis1=[lis[i] for i in range(0,length,3)]
    lis2=[int(lis[i]) for i in range(1,length,3)]
    lis3=[int(lis[i]) for i in range(2,length+1,3)]
    num1=sum(lis2)
    num2=sum(lis3)
    #print '%s:%d,%d'.ljust(10) %(cAlign('今天总计',8),num1,num2)
    print '%s' %(fill_text_to_print_width('今天总计',20))
    for i in range(len(lis1)):
        #print '%s:%d/%d' %(cAlign(lis1[i],8),lis2[i],lis3[i])
        lis1[i]=fill_text_to_print_width(lis1[i],20)
        #print '%s' %(cAlign(lis1[i],7))
        print lis1[i]
if __name__=='__main__':
    main()