class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascal = [[1]*(i+1) for i in range(numRows)]
        for i in range(numRows):
            for j in range(1, i):
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        return pascal
#         if numRows == 0:
#             return None
#         if numRows == 1:
#             return [[1]]
#         if numRows == 2:
#             return [[1],[1,1]]
        
#         l1 = self.generate(numRows-1)
#         l2 = l1[numRows-2]

#         res = [0] * numRows
#         res[0] = 1
#         res[numRows-1] = 1
#         for i in xrange(1,numRows-1):
#             res[i] = l2[i-1]+l2[i]
#         l1.append(res)
#         return l1
        

class Solution(object):
    
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        self.res = []
        if numRows == 0:
            return
        self.generate1(numRows)
        return self.res
        
    def generate1(self, numRows):
        if numRows == 1:
            self.res.append([1])
            return [1]
        curr= [_ for _ in range(numRows)]
        last = self.generate1(numRows-1)
        curr[0], curr[-1] = 1, 1
        for i in range(1,numRows-1):
            curr[i] = last[i-1]+last[i]
        self.res.append(curr)
        return curr
         
        