class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sort, 奇数位相加
        nums.sort()
        # res = 0
        # for i in xrange(0,len(nums),2):
        #     res += nums[i]
        # return res
        return sum(nums[::2])