#!/usr/bin/python
#coding=utf-8
'''
stack类，实现栈的功能
Created on 2017年6月12日
@author: duoyi
'''

class pStack(object) :
    def __init__(self,size):#类的构造函数
        self.size = size
        self.stack = []

    def __str__(self):#类的输出方法
        return str(self.stack)

    def getSize(self) :#获取栈当前大小
        return len(self.stack)

    def push(self, x) :#入栈，栈满强制抛出自定义异常
        if self.isfull() :
            raise Exception("Stack is full！")
        self.stack.append(x)

    def pop(self) :#出栈，栈空强制抛出自定义异常
        if self.isempty() :
            raise Exception("Stack is empty！")
        topElement = self.stack[-1] 
        self.stack.remove(topElement)
        return topElement

    def isempty(self) :#判断栈空
        if len(self.stack) == 0 :
            return True
        return False

    def isfull(self) :#判断栈满
        if len(self.stack) == self.size :
            return True
        return False  
def main():
    tStack = pStack(5)
    print tStack.isempty()
    for num in range(5) :
        tStack.push(num)
    #tStack.push(5)   
    print tStack.getSize()
    print tStack
    print tStack.isfull()
    print tStack.pop()
if __name__ == '__main__':
    main()