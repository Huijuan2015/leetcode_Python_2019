class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # i,j -> j, n-i
        # 00->0,n-1,
        # 01->1,n-1

        # wrong solution: with extra space:
        # n = len(matrix)
        # res = [[_ for _ in range(n)] for _ in range(n)]
        # for i in range(n):
        #     for j in range(n):
        #         res[j][n-1-i] = matrix[i][j]
        # for i in range(n):
        #     for j in range(n):
        #         matrix[i][j] = res[i][j]
        # return matrix

        # 先对角翻转再左右翻转
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n): # 只需要操作一半
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for row in matrix:
            row.reverse()