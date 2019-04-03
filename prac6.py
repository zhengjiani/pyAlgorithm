# -*- coding: utf-8 -*-
# @Time    : 2019/4/3 22:30
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""
    输出旋转数组的最小元素
"""
def find_min(nums):
    """
    二分法
    :param nums:
    :return: int
    """
    #判断首尾重复元素，如果有则去重，右边指针不断前移直到不重复
    n = len(nums) - 1
    if n <0 :
        return -1
    while n > 0 and nums[n] == nums[0]:
        n -= 1
    if(nums[n] >= nums[0]):
        return nums[0]
    #否则二分
    l = 0
    r = n
    while l < r :
        mid = ( l + r )//2
        if nums[mid] < nums[0]:
            r = mid
        else:
            l = mid +1
    return nums[r]

if __name__ == "__main__":
    nums = [1,1,1,4,5,6,0,1,1]
    print(find_min(nums))