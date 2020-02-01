所求面积是几个方块的加减所得
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix: #or not matrix[]
            return 
        m, n = len(matrix), len(matrix[0])
        self.squareSum = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                self.squareSum[i][j] += matrix[i][j]
                if i-1 >= 0:
                    self.squareSum[i][j] += self.squareSum[i-1][j]
                if j-1 >= 0:
                    self.squareSum[i][j] += self.squareSum[i][j-1]
                if i-1>=0 and j-1>= 0:
                    self.squareSum[i][j] -= self.squareSum[i-1][j-1]
        
注意col1 row1的减一
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        res = self.squareSum[row2][col2]
        if row1-1>= 0:
            res -= self.squareSum[row1-1][col2]
        if col1-1 >= 0:
            res -= self.squareSum[row2][col1-1]
        if row1-1 >= 0 and col1-1 >= 0:
            res += self.squareSum[row1-1][col1-1]
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)