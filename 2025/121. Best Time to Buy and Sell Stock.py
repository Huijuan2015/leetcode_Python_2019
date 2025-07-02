class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        buy = 0
        for i in range(1, len(prices)):
            curr = prices[i]
            if curr > prices[buy]:
                res = max(res, curr-prices[buy])
            else:
                buy = i
        return res
