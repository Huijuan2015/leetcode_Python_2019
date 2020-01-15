class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # (i,j) ->(j, n-i)
        # x
        n = len(matrix)
        # res = [[_ for _ in range(n)] for _ in range(n)]
        # for i in range(n):
        #     for j in range(n):
        #         res[j][n-1-i] = matrix[i][j]
        # print res
        # return matrix
        
        #(i,j) = (j,i) then swap cols 对角线翻转然后左右翻转
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            c1, c2 = 0, n-1
            while c1 < c2:
                matrix[i][c1], matrix[i][c2] = matrix[i][c2],matrix[i][c1]
                c1 += 1
                c2 -= 1
        