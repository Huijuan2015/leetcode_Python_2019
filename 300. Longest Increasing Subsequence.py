class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp[i] : 截止i 最长的递增串
        dp = [1 for _ in range(len(nums))]
        res = 0
        for i in range(len(nums)):
            for j in range(i): 去前面找所有的小于i的数，加1比较
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            res = max(res, dp[i])
        # print res, dp
        return res