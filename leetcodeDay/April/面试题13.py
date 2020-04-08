# -*- encoding: utf-8 -*-
"""
@File    : 面试题13.py
@Time    : 2020/4/8 12:02 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
class Solution:
    """广度优先搜索"""
    def movingCount(self, m, n, k):
        from queue import Queue
        q = Queue()
        q.put((0,0))
        s = set()
        while not q.empty():
            x,y = q.get()
            if (x,y) not in s and 0<=x<m and 0<=y<n and self.digitsum(x)+self.digitsum(y)<=k:
                s.add((x,y))
                # 向右、向下搜索
                for nx,ny in [((x+1),y),(x,(y+1))]:
                    q.put((nx,ny))
        return len(s)
    def digitsum(self,n):
        ans = 0
        while n:
            ans += n%10
            n //= 10
        return ans

if __name__ == '__main__':
    m = 2
    n = 3
    k = 1
    s = Solution()
    print(s.monvingCount(m,n,k))