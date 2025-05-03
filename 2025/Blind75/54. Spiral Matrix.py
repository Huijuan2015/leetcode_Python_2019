class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return
        rBegin, rEnd = 0, len(matrix) - 1
        cBegin, cEnd = 0, len(matrix[0]) - 1
        res = []
        while rBegin <= rEnd and cBegin <= cEnd:
            for j in range(cBegin, cEnd+1):
                res.append(matrix[rBegin][j])
            rBegin += 1
            for i in range(rBegin, rEnd+1):
                res.append(matrix[i][cEnd])
            cEnd -= 1
            if rBegin <= rEnd:
                for j in reversed(range(cBegin, cEnd+1)):
                    res.append(matrix[rEnd][j])
            rEnd -= 1
            if cBegin <= cEnd:
                for i in reversed(range(rBegin, rEnd+1)):
                    res.append(matrix[i][cBegin])
            cBegin += 1
        return res
