# -*- encoding: utf-8 -*-
"""
@File    : prac56.py
@Time    : 2020/4/16 9:33 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
排序区间
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(interval[1],merged[-1][1])
        return merged

if __name__ == '__main__':
    lis = [[1,3],[2,6],[8,10],[15,18]]
    s = Solution()
    print(s.merge(lis))