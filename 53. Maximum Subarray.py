class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # currSum, sum
        #  currSum+i ?  加上当前数比当前数大，则加上当前数； 加上当前数比不上当前数，只要当前数
        # update sum
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