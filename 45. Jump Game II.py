class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        每次新起的ladder比原ladder长的时候，就keep这个ladder； 
        if not nums or len(nums) < 2:
            return 0
        ladder, stairs = nums[0], nums[0]
        jump = 1
        for i in range(1, len(nums)):
            if i == len(nums)-1:
                return jump
            if i+nums[i] > ladder:
                ladder = i+nums[i]
            stairs -= 1
            if stairs == 0:
                jump += 1
                stairs = ladder - i
        return jump

TLE
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [float('inf') for _ in range(len(nums))]
        dp[0] = 0
        for i in range(len(nums)):
            # i+1: i+nums[i]
            end = min(i+nums[i]+1, len(nums))
            for j in range(i+1, end):
                dp[j] = min(dp[j], dp[i]+1)
        return dp[-1]