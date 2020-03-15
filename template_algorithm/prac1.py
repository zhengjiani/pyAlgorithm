# 滑动窗口问题
"""
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。
示例:
输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
1
2
3
进阶:
如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
如果小于s，扩右，大于s,缩左
"""
class Solution:
    def minSubArray(self,s,nums):
        # 滑动窗口
        size = len(nums)
        # 特例
        if size == 0:
            return 0
        l = 0

        # 初始化，求最小，则设置一个不可能到达的值为初始值
        res = size+1
        cur_sum = 0
        for i in range(len(nums)):
            # 扩右
            cur_sum += nums[i]
            while cur_sum >= s:
                res = min(res,i-l+1)
                cur_sum -= nums[l]
                l += 1
        # 如果全部数组元素加起来都 < s ，即 res 的值没有被更新，根据题意返回 0
        if res == len(nums) + 1:
            return 0
        return res

if __name__ == "__main__":
    s = Solution()
    nums = [2,3,1,2,4,3]
    print(s.minSubArray(7,nums))