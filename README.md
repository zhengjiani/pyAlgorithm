# Python算法练习
主要以LeetCode为主
## 目录结构
```shell script
├── cook_book  # python cookbook练习
├── documentation
├── interview # 面试题练习
├── leetcode # leetcode散装练习
├── leetcodeDay # leetcode按月打卡练习2020
│   ├── April
│   ├── July
│   ├── June
│   ├── March
│   └── May
├── page # 数据结构与算法
├── template_algorithm
└── test # 算法测试案例
```

## 机考中python处理输入
console_input.py

## 刷题总结
未来将持续更新ing...

[【刷题LeetCode】奇妙动态规划——不同路径II](https://blog.csdn.net/nicezheng_1995/article/details/107149602)

[【刷题LeetCode】奇妙动态规划——最长有效括号](https://blog.csdn.net/nicezheng_1995/article/details/107120436)

[【刷题LeetCode】二叉树 数学计算](https://blog.csdn.net/nicezheng_1995/article/details/106069076)

[【刷题LeetCode】二分查找算法应用](https://blog.csdn.net/nicezheng_1995/article/details/105861371)

[【刷题LeetCode】四月题库总结](https://blog.csdn.net/nicezheng_1995/article/details/105679478)

[【刷题LeetCode】LFU缓存](https://blog.csdn.net/nicezheng_1995/article/details/105326520)


## Python查漏补缺
- 合并两个字典的映射<br>
```shell script
>>> from collections import ChainMap
    >>> baseline = {'music': 'bach', 'art': 'rembrandt'}
    >>> adjustments = {'art': 'van gogh', 'opera': 'carmen'}
    >>> list(ChainMap(adjustments, baseline))
    ['music', 'art', 'opera']
```
- Counter对象
提供计数的计数器<br>
纠结交互模式下的多行输入了好久，最后发现顺其自然敲就好了<br>
```shell script
 >>> from collections import Counter
>>> for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    ...      cnt[word] += 1
    ...
>>> cnt
Counter({'blue': 6, 'red': 4, 'green': 2})
```
返回一个列表，提供 n 个频率最高的元素和计数<br>
```shell script
>>> Counter('abracadabra').most_common(3)
    [('a', 5), ('b', 2), ('r', 2)]
```
- deque对象
```shell script
>>> from collections import deque
    >>> d = deque('ghi')
    >>> for elem in d:
    ...     print(elem.upper())
    ...
    G
    H
    I
    >>> d.append('j')
    >>> d.appendleft('p')
    >>> d
    deque(['p', 'g', 'h', 'i', 'j'])
    >>> list(reversed(d))
    ['j', 'i', 'h', 'g', 'p']
    >>> d.extend('jkl')
    >>> d
    deque(['p', 'g', 'h', 'i', 'j', 'j', 'k', 'l'])
```  
    
- 不可以从空队列中弹出元素
```shell script
>>> d.clear()
>>> d
deque([])
>>> d.pop()
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
IndexError: pop from an empty deque
```
    
- defaultdict
将序列作为键值对加入字典
```shell script
 >>> from collections import defaultdict
 >>> d = defaultdict(list)
 >>> d
 defaultdict(<class 'list'>, {})
 >>> s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
 >>> for k,v in s:
    ...     d[k].append(v)
    ...
 >>> sorted(d.items())
 [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
```
在 Python 中如果使用 Queue 结构，但因为它是为多线程之间安全交换而设计的，所以使用了锁，会导致性能不佳。因此在 Python 中可以使用 **deque** 的 **append() 和 popleft()** 函数来快速实现队列的功能。<br>




