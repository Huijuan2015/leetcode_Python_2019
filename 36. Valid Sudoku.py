class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #3个used 9*9 matrix
        row = [[False for i in range(9)] for j in range(9)]# 第n行，每行1~9是否被用过
        col = [[False for i in range(9)] for j in range(9)]
        block = [[False for i in range(9)] for j in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])-1
                    #第几个block
                    k = i/3*3 + j/3
                    if row[i][num] or col[j][num] or block[k][num]:
                        return False
                    row[i][num] = col[j][num] = block[k][num] = True
        return True



class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        seen = []
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c != '.':
                    seen += [(c,j),(i,c),(i/3,j/3,c)]
        return len(seen) == len(set(seen))
