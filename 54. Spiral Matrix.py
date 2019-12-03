class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return
        rBegin, rEnd, cBegin, cEnd = 0,  len(matrix)-1, 0, len(matrix[0])-1
        res = []
        while rBegin <= rEnd and cBegin <= cEnd:
            # right
            for j in range(cBegin, cEnd+1):
                res.append(matrix[rBegin][j])
            rBegin += 1
            # down
            for i in range(rBegin, rEnd+1):
                res.append(matrix[i][cEnd])
            cEnd -= 1
            # left
            if rBegin <= rEnd: 防止row比较少，先减完了重复打印
                for j in reversed(range(cBegin, cEnd+1)):
                    res.append(matrix[rEnd][j])
            rEnd -= 1
            # up
            if cBegin <= cEnd:
                for i in reversed(range(rBegin, rEnd+1)):
                    res.append(matrix[i][cBegin])
            cBegin += 1
        return res
            
        