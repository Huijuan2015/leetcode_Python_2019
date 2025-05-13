class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m, n = len(grid), len(grid[0])
        q = collections.deque()
        time = 0
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0 
        while q and fresh > 0:
            for _ in range(len(q)):
                i, j = q.popleft()
                for direction in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    x, y = i+direction[0], j+direction[1]
                    if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] != 1:
                        continue
                    else:
                        grid[x][y] = 2
                        q.append((x, y))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1