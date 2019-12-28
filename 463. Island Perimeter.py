class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #有相邻就-1
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res += (4- self.neighbor(grid, i, j))
        return res
    
    def neighbor(self, grid, i, j):
        m, n  = len(grid), len(grid[0])
        cnt = 0
        if i-1>=0 and grid[i-1][j] == 1:
            cnt+=1
        if i+1<m and grid[i+1][j] == 1:
            cnt+=1
        if j-1>=0 and grid[i][j-1] == 1:
            cnt+=1
        if j+1<n and grid[i][j+1] == 1:
            cnt+=1
        return cnt