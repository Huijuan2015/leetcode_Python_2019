0 dead -> dead     没有变化

1 live -> live　　   没有变化

2 live -> dead　　从live 变为 dead

3 dead -> live　　从dead 变为live


class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                cnt = 0
                for dir in [[-1,-1], [-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]:
                    x, y = i+dir[0], j+dir[1]
                    if x>=0 and x<m and y>=0 and y<n and (board[x][y] == 1 or board[x][y] == 2):
                        cnt += 1
                if board[i][j] == 0 and cnt == 3: # current is dead cell
                     board[i][j] = 3 # dead -> live
                elif board[i][j] == 1 and (cnt < 2 or cnt > 3): # current live cell
                     board[i][j] = 2;#live 变为 dead
                # print i,j, board[i][j]
        print board
        for i in range(m):
            for j in range(n):
                board[i][j] %= 2
                  
            
                                                        
                

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                cnt = 0
                for dir in [[-1,-1], [-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]:
                    x, y = i+dir[0], j+dir[1]
                    # only state 1 and 2: cell are live for previous state
                    if x>=0 and x<m and y>=0 and y<n and abs(board[x][y]) == 1:
                        cnt += 1
                if board[i][j] == 0 and cnt == 3: # current is dead cell
                     board[i][j] = 2 # dead -> live
                elif board[i][j] == 1 and (cnt < 2 or cnt > 3): # current live cell
                     board[i][j] = -1;
                # print i,j, board[i][j]
        print board
        for i in range(m):
            for j in range(n):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
            
                                                        
                