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
                res = max(res, prices[j] - prices[buy])
            j += 1
        return res

