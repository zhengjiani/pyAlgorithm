# -*- encoding: utf-8 -*-
"""
@File    : binary_search.py
@Time    : 2020/4/30 2:46 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
def search(nums,left,right,target):
    while left<right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            # 下一轮搜索区间[left,mid-1],向左区间搜索
            right = mid - 1
        else:
            # 下一轮搜索区间[mid+1,right],向右区间搜索
            left = mid + 1
    return -1
def search_2(nums,left,right,target):
    mid = left + (right - left) // 2
    mid1 = left + (right-left+1)//2

    print(mid,mid1)
    # while left<right:
    #     # 选择中位数时下取整
    #     mid = left + (right-left)//2
    #
    #     if check(mid):
    #         left = mid + 1
    #     else:
    #         right = mid - 1

def search_3(nums,left,right,target):
    def check(n):
        if nums[n] == target:
            return True
        else:
            return False
    while left<right:
        # 选择中位数时上取整
        mid = left + (right-left+1)//2
        if check(mid):
            right = mid - 1
        else:
            left = mid + 1
if __name__ == '__main__':
    nums = [4,5]
    print(search_2(nums,0,len(nums),5))

