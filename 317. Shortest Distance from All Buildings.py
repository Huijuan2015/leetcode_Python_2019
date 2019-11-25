class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r, c = len(grid), len(grid[0])
        self.pathsum = [[0 for _ in range(c)] for _ in range(r)]
        self.visitCnt = [[0 for _ in range(c)] for _ in range(r)]
        cityCnt = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    cityCnt += 1
                    self.bfs(grid, r, c, i, j)
                    
        res = float('inf')
        m, n = -1, -1
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0 and self.pathsum[i][j] < res and self.visitCnt[i][j] == cityCnt:
                    res = self.pathsum[i][j]
                    m, n = i, j
        # print self.pathsum
        # return res if self.visitCnt[m][n] == cityCnt else -1
        return res if res != float('inf') else -1
    
    BFS向四周找dist, 需要一个visited来阻止TLE，同时更新visited城市数，dist
    def bfs(self, grid, r, c, i, j): #curr path length to bld[i][j]
        level = [((i, j), 0)]
        visited = [[False for _ in range(c)] for _ in range(r)]
        while level:
            # print level
            nextLevel = []
            for pair in level:
                point, dist = pair
                i, j = point
                self.pathsum[i][j] += dist
                self.visitCnt[i][j] += 1
                if i+1 < r and grid[i+1][j] == 0 and not visited[i+1][j]:
                    nextLevel.append(((i+1, j), dist+1))
                    visited[i+1][j] = True
                if i-1 >=0 and grid[i-1][j] == 0 and not visited[i-1][j]:
                    nextLevel.append(((i-1, j), dist+1))
                    visited[i-1][j] = True
                if j-1 >=0 and grid[i][j-1] == 0 and not visited[i][j-1]:
                    nextLevel.append(((i, j-1), dist+1))
                    visited[i][j-1] = True
                if j+1 < c and grid[i][j+1] == 0 and not visited[i][j+1]:
                    nextLevel.append(((i, j+1), dist+1))
                    visited[i][j+1] = True
            level = nextLevel
          
        #print self.pathsum
            
                    
            