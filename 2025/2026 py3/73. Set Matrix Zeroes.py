class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #用2个set 记录应该为0的行列，然后修改 O(m+n)
        #用第一行当第一个set记录应该变0 的列
        #用第一列当第二个set记录应该变0 的行
        m, n  = len(matrix), len(matrix[0])
        first_col_has_zero = False
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_has_zero = True
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                    
        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0   
        if  first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0



w