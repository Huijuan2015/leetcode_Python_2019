class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        # from 一个坐标，有一条path 数值一直递减
        # 也就是：from 海洋，找一条一直递增的路径
        if not heights or not heights[0]:
            return []
        m, n = len(heights), len(heights[0])
        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]

        def dfs(i, j, visited, prev_height):
            if i < 0 or j < 0 or i >= m or j >= n or visited[i][j] or heights[i][j] < prev_height:
                return
            visited[i][j] = True
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x, y = i + dx, j + dy
                dfs(x, y, visited, heights[i][j])
        
        for i in range(m):
            dfs(i, 0, pacific, heights[i][0]) # 左边
            dfs(i, n-1, atlantic, heights[i][n-1]) # 右边
    
        for j in range(n):
            dfs(0, j, pacific, heights[0][j]) # 上边
            dfs(m-1, j, atlantic, heights[m-1][j]) # 下边
        
        res = []
         # 同时被两个海洋访问的点
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i, j])
        return res


