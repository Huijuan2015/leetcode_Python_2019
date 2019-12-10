class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        m, n  = len(board), len(board[0])
        cnt = 0
        for i in range(m):
            for j in range(n):
                #什么情况下才会count: 找到了最左上valid的一个X
                if board[i][j] == '.' or (i-1>=0 and board[i-1][j] == 'X') or (j-1>=0 and board[i][j-1] == 'X'):
                    continue
                cnt += 1
        return cnt