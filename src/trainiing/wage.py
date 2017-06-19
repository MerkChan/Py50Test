#! /usr/bin/env python
# _*_coding:utf-8_*_
'''
Bonuses according with performance.
Created on 2017年6月7日
@author: duoyi
'''
def wage(perfman):
    bonuses=0
    if perfman <= 10:
        bonuses=perfman*0.1
    elif 10<perfman<=20:
        bonuses=10*0.1+(perfman-10)*0.075
    elif 20<perfman<=40:
        bonuses=10*0.1+10*0.075+(perfman-20)*0.05
    elif 40<perfman<=60:
        bonuses=10*0.1+10*0.075+20*0.05+(perfman-40)*0.03
    elif 60<perfman<=100:
        bonuses=10*0.1+10*0.075+20*0.05+20*0.03+(perfman-60)*0.015
    else:
        bonuses=10*0.1+10*0.075+20*0.05+20*0.03+40*0.015+(perfman-60)*0.01
    return bonuses    
def main():
    perfman=int(raw_input('Input the performance:'))
    bonuses=wage(perfman)
    print bonuses
if __name__ == '__main__':
    main()