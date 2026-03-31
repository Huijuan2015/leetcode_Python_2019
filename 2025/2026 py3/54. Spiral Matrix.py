class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix[0]), len(matrix)

        rBegin, rEnd, cBegin, cEnd = 0, n-1, 0, m-1
        res = []

        while rBegin <= rEnd and cBegin <= cEnd:
            for i in range(cBegin, cEnd+1):
                res.append(matrix[rBegin][i])
            rBegin += 1
            for i in range(rBegin, rEnd+1):
                res.append(matrix[i][cEnd])
            cEnd -= 1
            if rBegin <= rEnd: #判断行有效，ex只有一行
                for i in range(cEnd, cBegin-1, -1):
                    res.append(matrix[rEnd][i])
            rEnd -= 1
            if cBegin <= cEnd:#判断列有效, ex 只有一列
                for i in range(rEnd, rBegin - 1, -1):
                    res.append(matrix[i][cBegin])
            cBegin += 1
        return res
            
        
