# -*- encoding: utf-8 -*-
"""
@File    : prac999.py
@Time    : 2020/3/26 12:31 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
车的可用捕获量
有一个白色车（rook）。也可能有空方块，白色的象（bishop）和黑色的卒（pawn）。
它们分别以字符 “R”，“.”，“B” 和 “p” 给出。大写字符表示白棋，小写字符表示黑棋。
车按国际象棋中的规则移动：它选择四个基本方向中的一个（北，东，西和南），然后朝那个方向移动，
直到它选择停止、到达棋盘的边缘或移动到同一方格来捕获该方格上颜色相反的卒。
另外，车不能与其他友方（白色）象进入同一个方格。
方向数组
"""
class Solution:
    def numRookCaptures(self, board):
        # cnt表示吃到卒的数量
        cnt, st, ed = 0, 0, 0
        # 方向数组的坐标轴
        dx,dy = [0,1,0,-1],[1,0,-1,0]
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    st, ed = i,j
        for i in range(4):
            step = 0
            while True:
                tx = st + step*dx[i]
                ty = ed + step*dy[i]
                if tx<0 or tx>=8 or ty<0 or ty>=8 or board[tx][ty] == 'B':
                    break
                if board[tx][ty] == 'p':
                    cnt += 1
                    break
                step += 1
        return cnt


if __name__ == '__main__':
    board = [[".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", "p", ".", ".", ".", "."],
             [".", ".", ".", "p", ".", ".", ".", "."],
             ["p", "p", ".", "R", ".", "p", "B", "."],
             [".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", "B", ".", ".", ".", "."],
             [".", ".", ".", "p", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", "."]]
    s = Solution()
    print(s.numRookCaptures(board))