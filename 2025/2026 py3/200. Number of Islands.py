class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        visited = [[0]*len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and not visited[i][j]:
                    self.dfs(grid, i, j, visited)
                    island += 1
        return island
        
    def dfs(self, grid, i, j, visited):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or visited[i][j] or grid[i][j] == '0':
            return
        visited[i][j] = 1
        for direction in [-1, 0], [1, 0], [0, -1], [0, 1]:
            x, y = direction[0] + i, direction[1] + j
            self.dfs(grid, x, y, visited)
            

可以用grid 代替visited

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    island += 1
        return island
        
    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        for direction in [-1, 0], [1, 0], [0, -1], [0, 1]:
            x, y = direction[0] + i, direction[1] + j
            self.dfs(grid, x, y)
            