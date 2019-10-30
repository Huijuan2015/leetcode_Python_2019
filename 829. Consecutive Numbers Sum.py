class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        import math
        count = 1
        end = int(math.sqrt(2*N)) + 1
        for k in range(2, end):
            if (N-((k*(k-1)/2))) % k == 0:
                count += 1
        return count
        
