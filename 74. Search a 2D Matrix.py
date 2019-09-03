class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # binary search
        if not matrix or not matrix[0]: return False 
        row = len(matrix)
        col = len(matrix[0])
        start = 0
        end = row*col - 1
        while start <= end:
            mid = start + (end-start)/2
            # row = mid/col if col != 0 else mid
            # col = mid%col if row != 0 else mid
            num = matrix[mid/col][mid%col]
            if target == num:
                return True
            elif target < num:
                end = mid - 1
            else:
                start  = mid + 1
        return False