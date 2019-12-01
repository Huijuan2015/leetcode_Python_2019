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
    def numIslandsBFS(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        count = 0
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == '1':
                    self.bfs(grid, i, j)
                    count += 1
        return count

    def bfs(self, grid, r, c):
        queue = collections.deque()
        queue.append((r, c))
        grid[r][c] = '0'
        while queue:
            directions = [(0,1), (0,-1), (-1,0), (1,0)]
            r, c = queue.popleft()
            for d in directions:
                nr, nc = r + d[0], c + d[1]    
                if self.is_valid(grid, nr, nc) and grid[nr][nc] == '1':
                    queue.append((nr, nc))
                    grid[nr][nc] = '0'


自己的土BFS
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        import collections
        if not grid:
            return 0
        count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.bfs(grid,i,j)#需要标记
                    count += 1
        return count
    
    def bfs(self, grid, i, j):
        m,n = len(grid), len(grid[0])
        queue = collections.deque() #queue 
        queue.append((i,j))
        grid[i][j] = '#'
        while queue:
            # directions = [(0,1), (0,-1), (-1,0), (1,0)]
            i, j = queue.popleft()
            # for d in directions:
            #if i-1>=0 and j-1>=0 and i+1<m and j+1<n:
            if i+1 < m and grid[i+1][j] == '1':
                queue.append((i+1, j))
                grid[i+1][j] = '#'
            if i-1 >= 0 and grid[i-1][j] == '1':
                queue.append((i-1, j))
                grid[i-1][j] = '#'
            if j+1 < n and grid[i][j+1] == '1':
                queue.append((i, j+1))
                grid[i][j+1] = '#'
            if j-1 >= 0 and grid[i][j-1] == '1':
                queue.append((i, j-1))
                grid[i][j-1] = '#'
   
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # dfs if 1: from every point, visited-> # 0-> stop ==> count ++
        if not grid:
            return 0
        visited = [[False for _ in range(len(grid))] for _ in range(len(grid[0]))]
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, visited, i, j)
                    count += 1
        return count
        
    def dfs(self, grid, visited, i, j):
        # visited[i][j] = True
        if grid[i][j] != '1':
            return
        grid[i][j] = '#'
        if i+1 < len(grid) and grid[i+1][j] == '1':
            self.dfs(grid, visited, i+1, j)
        if i-1 >= 0 and grid[i-1][j] == '1':
            self.dfs(grid, visited, i-1, j)
        if j+1 < len(grid[0]) and grid[i][j+1] == '1':
            self.dfs(grid, visited, i, j+1)
        if j-1 >= 0 and grid[i][j-1] == '1':
            self.dfs(grid, visited, i, j-1)
        
                     
    
                