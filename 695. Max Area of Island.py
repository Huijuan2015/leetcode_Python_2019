class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        维持一个变量做curr sum up, dfs 
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, self.dfs(grid, i, j))
        return res
    
    def dfs(self, grid, i, j):
        if grid[i][j] != 1:
            return 0
        grid[i][j] = 0
        curr = 1
        if i-1 >= 0 and grid[i-1][j] == 1:
            curr += self.dfs(grid, i-1, j)
        if i+1 < len(grid) and grid[i+1][j] == 1:
            curr += self.dfs(grid, i+1, j)
        if j-1 >= 0 and grid[i][j-1] == 1:
            curr += self.dfs(grid, i, j-1)
        if j+1 < len(grid[0]) and grid[i][j+1] == 1:
            curr += self.dfs(grid, i, j+1)
        return curr
                    