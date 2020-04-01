# -*- encoding: utf-8 -*-
"""
@File    : prac836.py
@Time    : 2020/3/18 8:38 AM
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
矩形重叠
"""
class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        x1,y1,x2,y2 = rec1
        x_1,y_1,x_2,y_2 = rec2
        if x2 <= x_1 or x1 >= x_2 or y1 >= y_2 or y2 <= y_1:
            return False
        else:
            return True

class Solution1:
    def isRectangleOverlap(self, rec1, rec2):
        # pythonic代码
        return not (rec1[2] <= rec2[0] or  # left
                    rec1[3] <= rec2[1] or  # bottom
                    rec1[0] >= rec2[2] or  # right
                    rec1[1] >= rec2[3])  # top

# 检查区域
# 如果两个矩形重叠，那么他们重叠的区域一定也是个矩形，代表了两个矩形与x轴平行的边（水平边）
# 投影到x轴上时会有交集，y轴同理，将问题看作一堆线段是否有交集
class Solution2(object):
    def isRectangleOverlap(self, rec1, rec2):
        # intersect表示取交集
        def intersect(p_left, p_right, q_left, q_right):
            return min(p_right, q_right) > max(p_left, q_left)
        return (intersect(rec1[0], rec1[2], rec2[0], rec2[2]) and
                intersect(rec1[1], rec1[3], rec2[1], rec2[3]))

if __name__ == '__main__':
    rec1 = [0,0,2,2]
    rec2 = [2,2,3,3]
    # rec1 = [0,0,1,1]
    # rec2 = [2,2,3,3]
    s = Solution()
    print(s.isRectangleOverlap(rec1,rec2))