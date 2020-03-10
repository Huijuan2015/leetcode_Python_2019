class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return
        m, n = len(matrix), len(matrix[0])
        r, c, k = 0, 0, 0
        res = [_ for _ in range(m*n)]
        dirs = [[-1,1],[1,-1]]
        for i in range(m*n):
            print r, c, k,
            res[i] = matrix[r][c]
            r += dirs[k][0]
            c += dirs[k][1]
            print r, c, k
            if r >= m:
                r = m-1
                c += 2
                k = 1-k
            if c >= n:
                c = n-1
                r += 2
                k = 1-k
            if r < 0:
                r = 0
                k = 1-k
            if c < 0:
                c = 0
                k = 1-k
        return res