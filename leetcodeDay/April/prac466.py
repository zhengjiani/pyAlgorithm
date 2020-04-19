# -*- encoding: utf-8 -*-
"""
@File    : prac466.py
@Time    : 2020/4/19 9:00 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if n1 == 0:
            return 0
        s1cnt, index, s2cnt = 0,0,0
        recall = dict()
        while True:
            s1cnt += 1
            for ch in s1:
                if ch == s2[index]:
                    index += 1
                    if index == len(s2):
                        s2cnt,index = s2cnt+1,0
            # 还没有找到循环节，所有的s1就用完了
            if s1cnt == n1:
                return s2cnt // n2
            # 出现了之前的index,表示找到了循环节
            if index in recall:
                s1cnt_prime,s2cnt_prime = recall[index]
                # 前s1cnt'个s1包含了s2cnt'个s2
                pre_loop = (s1cnt_prime,s2cnt_prime)
                # 以后的每(s1cnt-s1cnt')个s1包含了(s2cnt-s2cnt')个s2
                in_loop = (s1cnt-s1cnt_prime,s2cnt-s2cnt_prime)
                break
            else:
                recall[index] = (s1cnt,s2cnt)
        ans = pre_loop[1] + (n1-pre_loop[0]) // in_loop[0]*in_loop[1]
        # 暴力匹配
        rest = (n1-pre_loop[0]) % in_loop[0]
        for i in range(rest):
            for ch in s1:
                if ch == s2[index]:
                    index += 1
                    if index == len(s2):
                        ans,index = ans+1,0
        return ans // n2

if __name__ == '__main__':
    s1,n1 = "acb",4
    s2,n2 = "ab",2
    s = Solution()
    print(s.getMaxRepetitions(s1,n1,s2,n2))