class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        #标记escaped, 只要从borders = 'O' dfs 即可
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])
        
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m-1 or j == n-1 and board[i][j] == 'O':
                    self.dfs(board, m, n, i, j)
        # print board
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'E':
                    board[i][j] = 'O'
    def dfs(self, board, m, n, i, j):
        if board[i][j] != 'O':
            return
        board[i][j] = 'E'
        for dir in [[1,0], [-1,0],[0,1],[0,-1]]:
            x, y = i+dir[0], j+dir[1]
            if x >= 0 and y>=0 and x < m and y < n:
                self.dfs(board, m, n, x, y)

        