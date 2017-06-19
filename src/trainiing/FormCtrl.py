#! /usr/bin/env python
# _*_coding:utf-8_*_#解释器能识别中文
'''
格式控制，35题。
Created on 2017年6月13日
@author: duoyi
'''
def is_chinese(uchar):
    """判断一个unicode是否是汉字"""
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False
def cAlign(name,length=0,key='r'):  #中文右对齐
    slen,cn_count = len(name),0  
    if length != 0 and slen<length and key=='r':        
        if isinstance(name, str):  
            placeholder = ' ' 
            name = placeholder*(length-slen)+name 
        else:
            for u in name:
                if is_chinese(u):
                    cn_count += 1  
            placeholder = ' ' #ascii码范围内是相等的u‘a’=='a'
            name=placeholder * (length-cn_count - len(name))+name          
    return name

def main():      
    s=u'''师门任务20次,0,80
除魔任务20次,0,100
闹事妖怪10次,0,50
运镖任务5次,0,40
挖宝5次,0,40
角色升级1次,0,50
完成4次江湖悬赏令,10,40
任务链整摆环3次,0,90
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
    print '%s:%d/%d' %(cAlign(u'今天总计',18),num1,num2)
    for i in range(len(lis1)):
        print '%s:%d/%d' %(cAlign(lis1[i],18),lis2[i],lis3[i])
if __name__=='__main__':
    main()
