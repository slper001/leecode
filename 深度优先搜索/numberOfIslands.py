# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     numberOfIsland
   Description : 岛屿的数量
   Author :       机器灵砍菜刀
   Init Date：          2018/9/13
-------------------------------------------------
"""
"""
给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。

示例 1:

输入:
11110
11010
11000
00000

输出: 1
示例 2:

输入:
11000
11000
00100
00011

输出: 3
"""


class Solution:
    def numIsland(self,grid):
        """
        :param grid: List[List[str]]
        :return: int
        """
        if not grid or not grid[0]:
            return 0

        def dfs(grid, x, y, r, c):
            grid[x][y] = '-1'   # 将所在网格字符改变，后续递归改变相邻的网格字符
            if x>0 and grid[x-1][y]=='1':
                dfs(grid,x-1,y,r,c)
            if x<r-1 and grid[x+1][y]=='1':
                dfs(grid,x+1,y,r,c)
            if y>0 and grid[x][y-1]=='1':
                dfs(grid,x,y-1,r,c)
            if y<c-1 and grid[x][y+1]=='1':
                dfs(grid,x,y+1,r,c)
        r,c = len(grid), len(grid[0])
        counts = 0
        for x in range(r):
            for y in range(c):
                if grid[x][y]=='1':
                    dfs(grid,x,y,r,c)
                    counts +=1
        return counts

