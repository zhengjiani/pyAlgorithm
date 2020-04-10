# -*- encoding: utf-8 -*-
"""
@File    : prac151.py
@Time    : 2020/4/10 9:05 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
翻转字符串中的单词
"""
import collections


class Solution:
    """使用内置函数"""
    def reverseWords(self,str):
        res = str.strip(' ').split(' ')
        res = list(filter(None,res))
        res.reverse()
        print(res)
        str = " ".join(res)
        return str

class Solution1:
    """自己编写对应函数
    1.对于字符串不可变的语言，需要将字符串转变为其他可变的数据结构，同时还需要在转化的过程中去除空格
    - 去除空格、翻转整个数组
    - 翻转每个单词
    - join
    2.对于字符串可变的语言，可以原地转
    - 翻转字符串
    - 翻转每一个单词
    - 去除无用空格
    """
    def reverseWords(self, s):
        l = self.trim_spaces(s)
        self.reverse(l,0,len(l)-1)
        self.reverse_each_word(l)
        return ''.join(l)

    def trim_spaces(self,s):
        left,right = 0,len(s)-1
        # 去除字符串开头的空白字符
        while left <= right and s[left] == ' ':
            left += 1
        # 去除字符串末尾的空白字符
        while left<= right and s[right] == ' ':
            right -= 1
        # 去除字符串间多余的空格
        output = []
        while left <= right:
            if s[left] != ' ':
                output.append(s[left])
            elif output[-1] != ' ':
                output.append(s[left])
            left += 1
        return output

    def reverse(self,l:list,left:int,right:int):
        while left < right:
            l[left],l[right] = l[right],l[left]
            left,right = left+1,right-1

    def reverse_each_word(self,l:list):
        n = len(l)
        start = end = 0
        while start < n:
            # 循环至单词末尾
            while end<n and l[end] != ' ':
                end += 1
            # 翻转单词
            self.reverse(l,start,end-1)
            # 更新start,寻找下一个单词
            start = end + 1
            end += 1

class Solution2:
    """双端队列，一个一个单词处理，并将单词压入队列头部"""
    def reverseWords(self, s):
        left, right = 0, len(s) - 1
        # 去掉字符串开头的空白字符
        while left <= right and s[left] == ' ':
            left += 1

        # 去掉字符串末尾的空白字符
        while left <= right and s[right] == ' ':
            right -= 1

        d, word = collections.deque(), []
        # 将单词 push 到队列的头部
        while left <= right:
            if s[left] == ' ' and word:
                d.appendleft(''.join(word))
                word = []
            elif s[left] != ' ':
                word.append(s[left])
            left += 1
        d.appendleft(''.join(word))

        return ' '.join(d)



if __name__ == '__main__':
    str = "  hello world!  "
    str1 = "a good    example"
    s = Solution1()
    print(s.reverseWords(str1))