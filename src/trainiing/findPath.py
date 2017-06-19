#! /usr/bin/env python
# _*_coding:utf-8_*
'''
34题，根据出发点和终点寻找路径。
#搜索算法，无思路
Created on 2017年6月14日
Simboard
@author: duoyi
'''
DATA={
    "中州城":("师道殿","云梦泽","逐风原","清水湾","千魂塔一层","帮派地图"),
    "北漠城":("鸣沙州","百花谷"),
    "月牙湾":("云梦泽","伏波港"),
    "伏波港":("月牙湾","百花谷"),
    "鸣沙州":("北漠城","苍茫山"),
    "逐风原":("平安镇","中州城"),
    "百花谷":("北漠城","伏波港"),
    "千魂塔一层":("千魂塔二层","中州城"),
    "云梦泽":("月牙湾","中州城"),
    "苍茫山":("鸣沙州"),
    "清水湾":("中州城","平安镇"),
    "师道殿":("绝情谷","真武门","蛮王殿","中州城","药王宗","天策府","拜火教","清虚观"),
    "清虚观":("师道殿"),
    "真武门":("师道殿"),
    "拜火教":("师道殿"),
    "绝情谷":("师道殿"),
    "蛮王殿":("师道殿"),
    "药王宗":("师道殿"),
    "千魂塔二层":("师道殿"),
    "平安镇":("清水湾","逐风原"),
    "帮派地图":("中州城")
    }
flag=[]
setName=[]
def findPath(source,destination):
    path=[]
    if source in DATA and destination in DATA:
        if source in setName:
            return path
        path.append(source)
        setName.append(source)
        nextm=DATA[source]
        if isinstance(nextm, tuple):
            nextiter=nextm
        else:
            nextiter=[]
            nextiter.append(nextm)
        if destination in nextiter:
            path.append(destination)
            return path
        else:
            for each in nextiter:
                nextSource=each
                Papepnd=findPath(nextSource, destination)
                if Papepnd is None:
                    setName.remove(source)
                flag.append(path.append(Papepnd))
            return flag
            
def main():
    path=findPath("中州城","清水湾")
    for each in path:
        print each,

if __name__ == '__main__':
    main()