和coin 2 统一：
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount+1): # amount i => dp[i]
                dp[i] = min(dp[i-coin]+1, dp[i])
        # print dp
        return dp[amount] if dp[amount] != float('inf') else -1
        


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0] + [float('inf')] * amount
        for i in range(1, amount+1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i-coin]+1) 使用当前coin后还剩余的amount+1 次
        
        return dp[-1] if dp[-1] != float('inf') else -1