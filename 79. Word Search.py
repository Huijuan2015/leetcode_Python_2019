class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # for word
        # dfs
        for i in range(len(board)):
            for j in range(len(board[0])):
                
                if self.findWord(board, word, i, j):
                    return True
        return False
            
    def findWord(self, board, word, i, j):

        #stop 条件：
        # i，j出界;idx>word length;visited
        if not word:
            return True
        if i<0 or i>=len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
            return False
        tmp = board[i][j]
        board[i][j] = '#'
        这样同时跑，立刻返回，减少时间
        res = self.findWord(board, word[1:], i-1, j) or self.findWord(board, word[1:], i+1, j) or self.findWord(board, word[1:], i, j-1) or self.findWord(board, word[1:], i, j+1)
        board[i][j] = tmp
        return res
    