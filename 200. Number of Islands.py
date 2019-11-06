class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count
    def dfs(self, grid, i, j):
        if i<0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return 
        grid[i][j] = '#'  # dfs to mark all adjacent islands
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
        
        # BFS?
    def bfs(self, grid, i, j):
        q =[(i, j)]
        grid[i][j] = "#"
        for i, j in q:
            for x, y in (i+1,j), (i-1, j), (i, j+1), (i, j-1):
                if 0 <= x < m and 0 <= y < n and grid[x][y] == "1":
                    grid[x,y] = "#"
                    q.append((x, y))
        return 1
                