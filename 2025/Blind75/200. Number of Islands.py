class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        cnt = 0
        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != '1':
                return
            grid[i][j] = '#'
            for dir in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                x, y = i + dir[0], j +dir[1]
                dfs(x, y)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    cnt += 1
        return cnt


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        numIslands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    numIslands += 1
        return numIslands
    
    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
        for direction in directions:
            x, y = i+direction[0], j+direction[1]
            self.dfs(grid, x, y)
