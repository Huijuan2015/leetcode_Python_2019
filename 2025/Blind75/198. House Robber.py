class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp[i] max money i can get
        # dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        if not nums:
            return 0

        if len(nums) < 2:
            return nums[0]
        n = len(nums)
        dp = [float('-inf')] * (n+1)
        dp[0], dp[1] = 0, nums[0]
        for i in range(2, n+1):
            print i, i-1, i-2
            dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])
        return dp[n]

same，移除index 0
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp[i] max money i can get
        # dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        if not nums:
            return 0

        if len(nums) <= 2:
            return max(nums)
        n = len(nums)
        dp = [float('-inf')] * n
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[n-1]
