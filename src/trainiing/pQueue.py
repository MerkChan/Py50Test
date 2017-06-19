#!/usr/bin/python
#coding=utf-8
'''
queue类，实现队列的功能
Created on 2017年6月12日
@author: duoyi
'''
class pQueue(object) :
    def __init__(self, size) :#构造函数
        self.size = size
        self.queue = []

    def __str__(self) :#输出
        return str(self.queue)

 
    def getSize(self) : #获取队列的当前长度
        return len(self.queue)

    def enqueue(self, items) :#入队，如果队列满了抛出异常，否则将元素插入队列尾
        if self.isfull() :
            raise Exception("Queue is full！")
        self.queue.append(items)

    def dequeue(self) :#出队，如果队列空了返回-1或抛出异常，否则返回队列头元素并将其从队列中移除
        if self.isempty() :
            raise Exception("Queue is empty！")
        firstElement = self.queue[0]
        self.queue.remove(firstElement)
        return firstElement

    def isfull(self) :#判断队列满
        if len(self.queue) == self.size :
            return True
        return False

    def isempty(self) : #判断队列空
        if len(self.queue) == 0 :
            return True
        return False
def main():
    tQueue = pQueue(5)
    print tQueue.isempty()
    for num in range(5) :
        tQueue.enqueue(num)
    tQueue.enqueue(5)   
    print tQueue.getSize()
    print tQueue
    print tQueue.isfull()
    print tQueue.dequeue()
if __name__ == '__main__':
    main()