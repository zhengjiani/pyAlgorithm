# -*- encoding: utf-8 -*-
"""
@File    : prac945.py
@Time    : 2020/3/22 9:25 AM
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
使数组唯一的最小增量
给定整数数组 A，每次 move 操作将会选择任意 A[i]，并将其递增 1。
返回使 A 中的每个值都是唯一的最少操作次数。
计数、排序、线性探测
"""
class Solution:
    def minIncrementForUnique(self, A):
        # 排序后贪心算法,贪心算法在于每个子问题的局部最优解会指向全局最优解。
        # 显然在对数组排序之后，可以通过保证数组的最后一个元素，经过+1操作后比前面所有元素大即可,此时子问题的最优解会收敛于全局最优解
        # 作者：cui-jin-hao-_official
        # 链接：https://leetcode-cn.com/problems/minimum-increment-to-make-array-unique/solution/python-tan-xin-suan-fa-by-cui-jin-hao-_official-3/
        # 来源：力扣（LeetCode）
        # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        A.sort()
        count = 0
        for i in range(1,len(A)):
            if A[i] <= A[i-1]:
                count += A[i-1] - A[i] + 1
                A[i] = A[i-1] + 1
        return count



if __name__ == '__main__':
    A = [1,2,2]
    s = Solution()
    print(s.minIncrementForUnique(A))