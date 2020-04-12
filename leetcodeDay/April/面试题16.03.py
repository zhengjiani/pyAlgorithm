# -*- encoding: utf-8 -*-
"""
@File    : 面试题16.03.py
@Time    : 2020/4/12 12:47 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
交点
"""
class Solution:
    """参数方程式
    x = x_1 + t(x_2 - x_1)
    y = y_1 + t(y_2 - y_1) t[0,1]
    """
    def intersection(self, start1, end1, start2, end2):
        # 判断（xk,yk）是否在线段（x1,y1）-（x2,y2）上
        # 这里的前提是（xk,yk）一定在直线（x1,y1）-（x2,y2）上
        def inside(x1,y1,x2,y2,xk,yk):
            # 若与x轴平行，则只需要判断x轴的部分
            # 若与y轴平行，则只需要判断y轴的部分
            # 普通线段则两者都要判断
            return (x1 == x2 or min(x1,x2) <= xk <= max(x1,x2)) \
                   and (y1 == y2 or min(y1,y2) <= yk <= max(y1,y2))

        def update(ans,xk,yk):
            # 将一个交点与当前ans中的结果相比较，找出最优的
            return [xk,yk] if not ans or [xk,yk] < ans else ans

        x1,y1 = start1
        x2,y2 = end1
        x3,y3 = start2
        x4,y4 = end2

        ans = list()
        # 判断（x1,y1）-（x2,y2）和（x3,y3）-（x4,y4）是否平行
        if (y4-y3)*(x2-x1) == (y2-y1)*(x4-x3):
            # 若平行，再判断（x3,y3）是否在直线（x1,y1）-(x2,y2)上
            if (y2-y1)*(x3-x1) == (y3-y1)*(x2-x1):
                # 判断（x3,y3）是否在线段（x1,y1）-(x2,y2)上
                if inside(x1,y1,x2,y2,x3,y3):
                    ans = update(ans,x3,y3)
                # 判断（x4,y4）是否在线段（x1,y1）-(x2,y2)上
                if inside(x1, y1, x2, y2, x4, y4):
                    ans = update(ans, x4, y4)
                # 判断（x1,y1）是否在线段（x3,y3）-(x4,y4)上
                if inside(x3, y3, x4, y4, x1, y1):
                    ans = update(ans, x1, y1)
                # 判断（x2,y2）是否在线段（x3,y3）-(x4,y4)上
                if inside(x3, y3, x4, y4, x2, y2):
                    ans = update(ans, x2, y2)
        else:
            # 联立方程得到t1和t2的值
            t1 = (x3 * (y4 - y3) + y1 * (x4 - x3) - y3 * (x4 - x3) - x1 * (y4 - y3)) / (
                        (x2 - x1) * (y4 - y3) - (x4 - x3) * (y2 - y1))
            t2 = (x1 * (y2 - y1) + y3 * (x2 - x1) - y1 * (x2 - x1) - x3 * (y2 - y1)) / (
                        (x4 - x3) * (y2 - y1) - (x2 - x1) * (y4 - y3))
            # 判断 t1 和 t2 是否均在 [0, 1] 之间
            if 0.0 <= t1 <= 1.0 and 0.0 <= t2 <= 1.0:
                ans = [x1 + t1 * (x2 - x1), y1 + t1 * (y2 - y1)]

        return ans
if __name__ == '__main__':
    line1 = {0, 0}, {1, 0}
    line2 = {1, 1}, {0, -1}
    start1 = [0, 0]
    end1 = [1,0]
    start2 = [1,1]
    end2 = [0,-1]
    s = Solution()
    print(s.intersection(start1,end1,start2,end2))