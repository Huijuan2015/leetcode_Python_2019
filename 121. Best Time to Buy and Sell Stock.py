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
                