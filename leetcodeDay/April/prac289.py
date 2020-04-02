# -*- encoding: utf-8 -*-
"""
@File    : prac289.py
@Time    : 2020/4/2 9:37 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态：1 即为活细胞（live），或 0 即为死细胞（dead）。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：
如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
根据当前状态，写一个函数来计算面板上所有细胞的下一个（一次更新后的）状态。下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/game-of-life
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def gameOfLife(self, board):
        """
        不返回任何值，仅就地修改细胞板子
        """
        # 八个相邻位置
        neighbors = [(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1)]

        rows = len(board)
        cols = len(board[0])

        # 复制原数组,作为规则引用
        copy_board = [[board[row][col] for col in range(cols)] for row in range(rows)]

        #双层循环遍历数组
        for row in range(rows):
            for col in range(cols):
                # 对于每一个细胞统计其八个相邻位置活细胞数量
                live_neighbors = 0
                for neighbor in neighbors:

                    r = (row + neighbor[0])
                    c = (col + neighbor[1])

                    # 查看相邻的细胞是否为活细胞
                    if (r<rows and r>=0) and (c<cols and c>=0) and (copy_board[r][c]==1):
                        live_neighbors += 1

                # 如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
                # 如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
                if copy_board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[row][col] = 0
                # 如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
                if copy_board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 1

class Solution1:
    """定义复合状态，原地改变数组
        例子：如果细胞之前的状态是 0，但是在更新之后变成了 1，我们就可以给它定义一个复合状态 2
    """
    def gameOfLife(self, board):
        # 八个相邻位置
        neighbors = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]

        rows = len(board)
        cols = len(board[0])

        # 双层循环遍历数组
        for row in range(rows):
            for col in range(cols):
                # 对于每一个细胞统计其八个相邻位置活细胞数量
                live_neighbors = 0
                for neighbor in neighbors:

                    r = (row + neighbor[0])
                    c = (col + neighbor[1])

                    # 查看相邻的细胞是否为活细胞
                    if (r < rows and r >= 0) and (c < cols and c >= 0) and (abs(board[r][c]) == 1):
                        live_neighbors += 1

                # 如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
                # 如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
                if board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    # -1代表这个细胞过去是火的现在死了
                    board[row][col] = -1
                # 如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
                if board[row][col] == 0 and live_neighbors == 3:
                    # 2代表这个细胞过去是死的现在活了
                    board[row][col] = 2

        # 遍历board得到一次更新后的状态
        for row in range(rows):
            for col in range(cols):
                if board[row][col] > 0:
                    board[row][col] = 1
                else:
                    board[row][col] = 0

if __name__ == '__main__':
    board = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0]
    ]
    s = Solution1()
    s.gameOfLife(board)
    print(board)