class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 上下翻转 然后对角线翻转
        m = len(matrix)
        for i in range(m//2): #整行
            matrix[i], matrix[m-1-i] =  matrix[m-1-i], matrix[i]
        for i in range(m):
            for j in range(i+1, m): #只交换对角线一侧的元素
                if i < j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

