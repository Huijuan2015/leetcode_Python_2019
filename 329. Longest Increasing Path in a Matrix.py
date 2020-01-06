class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        self.dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        if not matrix or not matrix[0]:
            return 0
        m, n  = len(matrix), len(matrix[0])
        self.visited = [[-1 for _ in range(n)] for _ in range(m)]
        res = float('-inf')
        for i in range(m):
            for j in range(n):
                res = max(res, self.dfs(matrix, i, j))
        return res
    
    def dfs(self, matrix, i, j): # return max length
        if self.visited[i][j] != -1:
            return self.visited[i][j]
        length = 0
        # if i+1 < len(matrix) and matrix[i+1][j] > matrix[i][j]:
        #     length = max(length, self.dfs(matrix, i+1, j))
        # if i-1 >= 0 and matrix[i-1][j] > matrix[i][j]:
        #     length = max(length, self.dfs(matrix, i-1, j))
        # if j+1 < len(matrix[0]) and matrix[i][j+1] > matrix[i][j]:
        #     length = max(length, self.dfs(matrix, i, j+1))
        # if j-1 >= 0 and matrix[i][j-1] > matrix[i][j]:
        #     length = max(length, self.dfs(matrix, i, j-1))
        for dir in self.dirs:
            x, y = dir[0]+i, dir[1]+j
            if x<0 or x>= len(matrix) or y<0 or y>= len(matrix[0]) or matrix[x][y]<= matrix[i][j]:
                continue
            # print x, y
            length = max(length, self.dfs(matrix, x, y))
        self.visited[i][j] = length+1
        return length + 1   
        
        
        
        
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        m, n  = len(matrix), len(matrix[0])
        self.visited = [[-1 for _ in range(n)] for _ in range(m)]
        res = float('-inf')
        for i in range(m):
            for j in range(n):
                res = max(res, self.dfs(matrix, i, j))
        return res
    
    def dfs(self, matrix, i, j): # return max length
        if self.visited[i][j] != -1:
            return self.visited[i][j]
        length = 0
        if i+1 < len(matrix) and matrix[i+1][j] > matrix[i][j]:
            length = max(length, self.dfs(matrix, i+1, j))
        if i-1 >= 0 and matrix[i-1][j] > matrix[i][j]:
            length = max(length, self.dfs(matrix, i-1, j))
        if j+1 < len(matrix[0]) and matrix[i][j+1] > matrix[i][j]:
            length = max(length, self.dfs(matrix, i, j+1))
        if j-1 >= 0 and matrix[i][j-1] > matrix[i][j]:
            length = max(length, self.dfs(matrix, i, j-1))
        self.visited[i][j] = length+1
        return length + 1   
        
        
        
        