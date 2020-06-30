# -*- encoding: utf-8 -*-
"""
@File    : 面试题16.18.py
@Time    : 2020/6/30 9:03 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        count_a = sum(1 for ch in pattern if ch == 'a')
        count_b = len(pattern) - count_a
        # 保证了a出现了至少一次c_a > 0,这样枚举l_a就不会有问题
        if count_a < count_b:
            count_a, count_b = count_b, count_a
            pattern = ''.join('a' if ch == 'b' else 'b' for ch in pattern)

        # value为空，要求pattern也为空l_p = 0或者只出现了字母a(l_p - c_a = 0)
        if not value:
            return count_b == 0
        # 如果pattern为空且value不为空，无法匹配成功
        if not pattern:
            return False

        # c_a*l_a + (l_p - c_a)*l_b = l_v
        # 直接枚举l_a的值，它必须是[0,l_v/c_a]之间的自然数
        for len_a in range(len(value) // count_a + 1):
            rest = len(value) - count_a * len_a
            if (count_b == 0 and rest == 0) or (count_b != 0 and rest % count_b == 0):
                len_b = 0 if count_b == 0 else rest // count_b
                # 当遍历到一个a时，取出从pos开始，长度为l_a的子串
                # - 第一次遇到字母a，就得到a对应的子串
                # - 将取出的子串与a进行比较，如果不相同，说明模式匹配失败
                pos, correct = 0, True
                value_a, value_b = None, None
                for ch in pattern:
                    if ch == 'a':
                        sub = value[pos:pos+len_a]
                        if not value_a:
                            value_a = sub
                        elif value_a != sub:
                            correct = False
                            break
                        pos += len_a
                    else:
                        sub = value[pos:pos+len_b]
                        if not value_b:
                            value_b = sub
                        elif value_b != sub:
                            correct = False
                            break
                        pos += len_b
                if correct and value_a != value_b:
                    return True
        return False

if __name__ == '__main__':
    pattern = "abba"
    value = "dogcatcatdog"
    sl = Solution()
    print(sl.patternMatching(pattern,value))