class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0 for _ in range(amount+1)]

        dp[0] = 1
        # for i in range(1, amount+1):
        #     for coin in coins:
        #         if i-coin >= 0:
        #             dp[i] += dp[i-coin]
        for coin in coins:
            for i in range(coin, amount+1): 注意里外循环
                dp[i] = dp[i] + dp[i-coin]
        return dp[amount]


TLE
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # dfs
        if not coins:
            return 1 if amount == 0 else 0
        self.cnt = 0
        visited = set()
        self.findPath(amount, len(coins)-1, coins, "", visited)
        return self.cnt
        
    def findPath(self, remain, i, coins, path, visited):
        if remain < 0 or i < 0:
            return
        if remain == 0 and path not in visited:
            self.cnt += 1
            visited.add(path)
            return
        coin = coins[i]
        self.findPath(remain-coin, i, coins, path+str(coin), visited)
        self.findPath(remain, i-1, coins, path, visited)   
        