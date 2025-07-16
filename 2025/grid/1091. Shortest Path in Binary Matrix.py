class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #最短路径用BFS
        if not grid:
            return 0
        
        n = len(grid)
        queue = deque()
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1
        queue.append((0, 0, 1))
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      ( 0, -1),          ( 0, 1),
                      ( 1, -1), ( 1, 0), ( 1, 1)]
        while queue:
            i, j, length = queue.popleft()
            if i == n - 1 and j == n - 1:
                return length
            for dir in directions:
                x, y = i + dir[0], j + dir[1]
                
                if 0 <= x < n and 0<= y < n and grid[x][y] == 0:
                    queue.append((x, y, length + 1))
                    grid[x][y] = 1
        return -1


        