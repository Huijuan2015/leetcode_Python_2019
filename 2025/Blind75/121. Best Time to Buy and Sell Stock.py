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


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) < 2:
            return 0
        buy, profit = 0, 0
        sell = 1
        while sell < len(prices):
            if prices[sell] > prices[buy]:
                profit = max(profit, prices[sell] - prices[buy])
            else:
                buy = sell
            sell += 1
        return profit