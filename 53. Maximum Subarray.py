class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        ret = nums[0]
        curr = ret
        # if not nums:
        #     return 0
        for num in nums[1:]:
            # if curr+num > num:
            #     curr += num
            # else:
            #     curr = num
            curr = max(num, curr+num)
            ret = max(ret, curr)
        return ret