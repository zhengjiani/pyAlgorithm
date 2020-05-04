# -*- encoding: utf-8 -*-
"""
@File    : prac45.py
@Time    : 2020/5/4 9:11 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from typing import List


class Solution:
    """反向查找出发位置
    python会超时
    """
    def jump(self, nums: List[int]) -> int:
        pass
class Solution1:
    """正向查找可到达最大长度
    维护当前能够到达的最大下标位置
    """
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos,end,step = 0,0,0
        for i in range(n-1):
            if maxPos >= i:
                maxPos = max(maxPos,i+nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step
if __name__ == '__main__':
    nums = [2,3,1,1,4]
    s = Solution1()
    print(s.jump(nums))