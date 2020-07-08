# -*- encoding: utf-8 -*-
"""
@File    : 面试题16.11.py
@Time    : 2020/7/8 9:07 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from typing import List


class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        res = []
        if not k:
            return []
        if shorter == longer:
            res.append(k*shorter)
        res.extend([k*shorter,k*longer])
        # shorter + k - shorter
        # 假设shorter数量为i,longer数量k-i
        for i in range(1,k):
            res.append(shorter*i + longer*(k-i))
        return sorted(res)

if __name__ == '__main__':
    sl = Solution()
    shorter = 1
    longer = 2
    print(sl.divingBoard(1,1,0))
