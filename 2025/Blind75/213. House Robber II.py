class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp[i]
        # 1.	不偷最后一间房子 → 从 nums[0] 到 nums[n-2]
	    # 2.	不偷第一间房子 → 从 nums[1] 到 nums[n-1]

        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        n = len(nums)

        dp1 = [0] * (n - 1)
        dp1[0], dp1[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n-1):
            dp1[i] = max(dp1[i-1], dp1[i-2]+nums[i])
        
        dp2 = [0] * (n - 1)
        dp2[0], dp2[1] = nums[1], max(nums[1], nums[2])
        for i in range(2, n-1):
            dp2[i] = max(dp2[i-1], dp2[i-2]+nums[i+1])
        return max(dp1[-1], dp2[-1])

cleaner:
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp[i]
        # 1.    不偷最后一间房子 → 从 nums[0] 到 nums[n-2]
        # 2.    不偷第一间房子 → 从 nums[1] 到 nums[n-1]

        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        n = len(nums)

        def rob(houses):
            dp = [0] * (n - 1)
            dp[0], dp[1] = houses[0], max(houses[0], houses[1])
            for i in range(2, n-1):
                dp[i] = max(dp[i-1], dp[i-2]+houses[i])
            return dp[-1]
        
        return max(rob(nums[1:]), rob(nums[:-1]))