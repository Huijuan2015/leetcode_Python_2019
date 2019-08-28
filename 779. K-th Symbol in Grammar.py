class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """

            
        if N <= 1 and K <=1:
            return 0
        
        # to find N,k
        # is to find N-1, K/2
        else:
            prev = self.kthGrammar(N-1, K//2) if K%2 == 0 else self.kthGrammar(N-1, K//2+1)
        #prev
        # 0  1
        # 01 10
        if (prev == 0 and K%2 != 0) or (prev ==  1 and K%2 == 0):
            return 0
        if (prev ==0 and K%2 == 0) or (prev == 1 and K%2 != 0):
            return 1