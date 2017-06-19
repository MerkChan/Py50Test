#! /usr/bin/env python
# _*_coding:utf-8_*_
'''
成绩排名，40题。
Created on 2017年6月13日
@author: duoyi
'''
def scoreRank(dic):
    dic_copy=dic.copy()
    for key in dic:
        if dic[key]<70:
            del dic_copy[key]
    lis=sorted(dic_copy.iteritems(), lambda x, y: cmp(x[1], y[1]), reverse = True)#key=lambda d:d[1]等效
    return lis


def main():
    dGrade={"王明":92,"李晓红":90,"张良":90,"刘大住":88,"贾城":76,
            "王小胖":66,"王英":59,"张军":66}
    lis=scoreRank(dGrade)
    for each in lis:
        print each[0],':',each[1],
if __name__ == '__main__':
    main()