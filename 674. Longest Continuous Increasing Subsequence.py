class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #i, j
        # if j<=i: sum = max(curr, sum), curr = 1
        # while i < j: ++
        #i-1, i
        if not nums:
            return 0
        curr = 1
        longest = curr
        
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                curr = 0
            curr += 1
            longest = max(longest, curr)
        return longest
            