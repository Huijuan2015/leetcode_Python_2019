class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        start = end = 0
        n = len(nums)
        curSum = 0
        minLen = n+1
        while start < n and end < n:
            while curSum < s and end < n:
                curSum += nums[end]
                end += 1
            while curSum >= s and start < n:
                minLen = min(minLen, end-start)
                curSum -= nums[start]
                start += 1
        return 0 if minLen == n+1 else minLen