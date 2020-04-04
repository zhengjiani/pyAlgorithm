# -*- encoding: utf-8 -*-
"""
@File    : prac42.py
@Time    : 2020/4/4 8:49 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
单调栈，单调队列
"""
class Solution:
    """按行求解，提交后超出时间限制"""
    def trap(self, height):
        sum = 0
        max_h = max(height)
        for i in range(1,max_h+1):
            # 标记是否开始更新
            is_start = False
            temp = 0
            for j in range(len(height)):
                 # 如果当前的高度小于 i，并且两边有高度大于等于 i 的，说明这个地方一定有水，水就可以加 1
                if is_start and height[j] < i:
                    temp += 1
                # 遇到高度大于等于 i 的，就把 temp 加到最终的答案 ans 里，并且 temp 置零，然后继续循环。
                if height[j] >= i:
                    sum = sum + temp
                    temp = 0
                    is_start = True
        return sum

    def get_max(self,height):
        """
        找到最大高度
        :param height:
        :return:
        """
        max_height = 0
        for i in range(len(height)):
            if height[i]>max_height:
                max_height = height[i]
        return max_height

class Solution1:
    """双指针求法"""
    def trap(self, height):
        n = len(height)
        if n == 0:
            return 0
        left = 0
        right = n -1
        # max_left [i] 代表第 i 列左边最高的墙的高度
        max_left = height[left]
        # max_right[i] 代表第 i 列右边最高的墙的高度
        max_right = height[right]
        ans = 0

        while(left < right):
            if max_left <= max_right:
                ans += max_left-height[left]
                left += 1
                max_left = max(height[left],max_left)
            if max_left > max_right:
                ans += max_right-height[right]
                right -= 1
                max_right = max(height[right],max_right)
        return ans

class Solution3:
    """栈的求法，类似括号匹配"""
    def trap(self, height):
        """
        将每堵墙作为栈元素入栈
        :param height:
        :return:
        """
        sum = 0
        stack = []
        current = 0
        while(current<len(height)):
            # 如果栈不空且当前高度大于栈顶高度就一直循环
            while(len(stack) != 0 and height[current] > height[stack[-1]]):
                h = height[stack[-1]]
                stack.pop()
                if len(stack) == 0:
                    break
                # 计算两堵墙之间的距离
                distance = current - stack[-1] - 1
                min_h = min(height[stack[-1]],height[current])
                sum = sum + distance * (min_h - h)
            stack.append(current)
            current += 1
        return sum

if __name__ == '__main__':
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    s = Solution3()
    print(s.trap(height))