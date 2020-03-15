# -*- coding: utf-8 -*-
# @Time    : 2019/9/14 13:42
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""
把数组排成最小的数，
第一种解法——用了全排列函数permutation
"""
class Solution:
    # 递归实现数组全排列
    nums = []
    def permutations(self,arr,position,end):
        if position == end:
            self.nums.append(self.PrintMinNumber(arr))
        else:
            for index in range(position,end):
                arr[index],arr[position] = arr[position],arr[index]
                self.permutations(arr,position+1,end)
                arr[index],arr[position] = arr[position],arr[index]

    def PrintMinNumber(self,numbers):
        lis = []
        for i in numbers:
            lis.append(str(i))
        str1 = "".join(lis)
        return int(str1)


if __name__ == "__main__":

    lis = [3,5,1,4,2]
    # print(s.PrintMinNumber(lis))
    # s = Solution()
    # s.permutations(lis,0,len(lis))
    # print(min(Solution.nums))
    s1 = Solution1()
    print(Solution1.PrintMinNumber(s1,lis))

