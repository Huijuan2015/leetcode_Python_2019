class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 
        if not matrix or not target:
            return False
        row, col = 0, len(matrix[0])-1
        while row < len(matrix) and col >= 0:
            num = matrix[row][col]
            if target == num:
                return True
            elif target > num:
                row += 1
            else:
                col -= 1 #smart
        return False    