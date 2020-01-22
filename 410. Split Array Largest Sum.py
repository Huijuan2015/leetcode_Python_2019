class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        dp[i][j]: 0~i 被分为j份时的最小的最大值
        n = len(nums)
        dp = [[float('inf') for _ in range(m+1)] for _ in range(n+1)]
        s = [0 for _ in range(n+1)]
        curr = 0
        dp[0][0] = 0
        for i in range(1, n+1):
            curr += nums[i-1]
            s[i] = curr
            for j in range(1, m+1):
                for k in range(i):
                    dp[i][j] = min(dp[i][j], max(dp[k][j-1], s[i]-s[k]))

        return dp[n][m]