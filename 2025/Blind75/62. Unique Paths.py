dfs+memo
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        memo = [[-1]*n for _ in range(m)]
       
        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return 0
            if i == m -1 and j == n -1:
                return 1
            if memo[i][j] != -1:
                return memo[i][j]
            memo[i][j] = dfs(i+1, j)+dfs(i, j+1)
            return memo[i][j]
        return dfs(0, 0)


单纯DFS超时X
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
       
        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return 0
            if i == m -1 and j == n -1:
                return 1
            return dfs(i+1, j) + dfs(i, j+1)
        return dfs(0, 0)