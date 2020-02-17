class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not len(matrix[0]):
            return 0
        m, n = len(matrix), len(matrix[0])
        res = 0
        visited = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                res = max(res, self.helper(matrix, i, j, visited))
        return res
        
    def helper(self, matrix, i, j, visited):#return min len of point [i][j]
        if visited[i][j] != 0:
            return visited[i][j]
        
        visited[i][j] = 1
        for dir in [[1,0], [-1,0],[0,1],[0,-1]]:
            x, y = i+dir[0], j+dir[1]
            if x < 0 or y < 0 or x >= len(matrix) or y >= len(matrix[0]) or matrix[x][y] <= matrix[i][j]:
                continue
            visited[i][j] = max(visited[i][j], self.helper(matrix, x, y, visited)+1) 别忘记＋1
        return visited[i][j]
        

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        visited = [[-1 for _ in range(n)] for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, self.dfs(matrix, m, n, i, j, visited)) 
        return res
        
    def dfs(self, matrix, m, n, i, j, visited): # return i,j 的最长递增长度
        if visited[i][j] != -1:
            return visited[i][j]
        visited[i][j] = max(1, visited[i][j]) => 不设置length，那要设定visited[i][j]默认值   或者写成visited[i][j] = 1
        for dir in [[0,1], [0,-1], [1,0], [-1, 0]]:
            x, y = dir[0]+i, dir[1]+j
            if x < 0 or x>= m or y < 0 or y >= n or matrix[x][y] <= matrix[i][j]:
                continue
            visited[i][j]= max(visited[i][j], self.dfs(matrix, m, n, x, y, visited)+1)
        return  visited[i][j]

        
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
        
        
        
        