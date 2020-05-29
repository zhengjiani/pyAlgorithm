# -*- encoding: utf-8 -*-
"""
@File    : prac974.py
@Time    : 2020/5/28 11:28 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
给定一个整数数组 A，返回其中元素之和可被 K 整除的（连续、非空）子数组的数目。
A = [4,5,0,-2,-3,1], K = 5,output:7
有 7 个子数组满足其元素之和可被 K = 5 整除：
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
"""
from typing import List

class Solution:
    """哈希表+逐一设计(同余定理)"""
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        # 以前缀和模 KK 的值为键，出现次数为值的哈希表 {record}
        record = {0:1}
        total,ans = 0,0
        for elem in A:
            total += elem
            modulus = total % K
            same = record.get(modulus,0)
            ans += same
            record[modulus] = same + 1
        return ans

class Solution1:
    """哈希表+单次统计，从排列组合的角度"""
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        record = {0:1}
        total = 0
        for elem in A:
            total += elem
            moduls = total % K
            record[moduls] = record.get(moduls,0) + 1

        ans = 0
        for x,cx in record.items():
            ans += cx * (cx-1)//2
        return ans

if __name__ == '__main__':
    A = [4, 5, 0, -2, -3, 1]
    K = 5
    s = Solution()
    print(s.subarraysDivByK(A,K))