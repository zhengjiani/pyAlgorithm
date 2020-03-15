# -*- coding: utf-8 -*-
# @Time    : 2019/9/4 11:15
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""
数组中出现次数超过一半的数字
"""
# 不调用库函数
# 假设有这个数字，那么它的数量一定比其它所有数字之和还要多
class Solution:
    def MoreThanHalfNum_Solution(self,numbers):
        if not numbers:
            return 0
        num = numbers[0]
        count = 1
        for i in range(1,len(numbers)):
            if numbers[i] == num:
                count += 1
            else:
                count -= 1
            if count == 0:
                num = numbers[i]
                count = 1
        count = 0
        for i in numbers:
            if i==num:
                count += 1
        return num if count > len(numbers) / 2.0 else 0

# 第二种调库的方法
class Solution1:
    def MoreThanHalfNum_Solution(self,numbers):
        from collections import Counter
        count = Counter(numbers).most_common()
        if count[0][1] > len(numbers)/2.0:
            return count[0][0]
        return 0
if __name__ == "__main__":
    lis = [1,2,3,2,2,2,5,4,2]
    s = Solution()
    print(s.MoreThanHalfNum_Solution(lis))
