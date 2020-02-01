class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = 0
        res, j = 0, 1
        while j < len(prices):
            if prices[j] < prices[buy]:
                buy = j
            else:
                res = max(res, prices[j]-prices[buy])
            j+=1
        return res

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) < 2:
            return 0
        buy = 0
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[buy]:
                res = max(res, prices[i] - prices[buy])
            else:
                buy = i
        return res
                