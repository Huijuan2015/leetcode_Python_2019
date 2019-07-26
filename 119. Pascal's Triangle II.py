class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        pascal = [1] * (rowIndex + 1)
        for i in range(2, rowIndex+1):
            for j in range(i-1, 0, -1):
                pascal[j] += pascal[j-1]
        return pascal
#         pascal = [[1]*(i+1) for i in range(rowIndex+1)]
#         for i in range(rowIndex+1):
#             for j in range(1, i):
#                 pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        
#         return pascal[rowIndex]