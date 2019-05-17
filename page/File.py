# -*- coding: utf-8 -*-
# @Time    : 2019/5/15 13:18
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
#读取纯文本文件
def main():
    f = None
    try:
        f = open('aaa.txt','r',encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件！')
    except LookupError:
        print('指定了未知的编码')
    except UnicodeDecodeError:
        print('读取文件时解码错误！')
    finally:
        if f:
            f.close()

    #通过with关键字指定文件对象的上下文环境并在离开上下文环境时自动释放文件资源
    try:
        with open('aaa.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件！')
    except LookupError:
        print('指定了未知的编码')
    except UnicodeDecodeError:
        print('读取文件时解码错误！')

    #for-in循环逐行读取，readlines方法将文件按行读取到一个列表容器中
    import time
    #通过for-in循环逐行读取
    with open('aaa.txt',mode='r') as f:
        for line in f:
            print(line,end='')
            time.sleep(0.5)
    print()

    #读取文件到列表中
    with open('aaa.txt') as f:
        lines = f.readlines()
    print(lines)

if __name__ == '__main__':
    main()