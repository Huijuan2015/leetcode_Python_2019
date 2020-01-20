class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        nums = [lower-1]+nums+[upper+1]
        res = []
        for i in range(len(nums)-1):
            left, right = nums[i], nums[i+1]
            if left != right-1:
                if right - left == 2:
                    res.append(str(left+1))
                elif right - left > 2 :
                    res.append(str(left+1)+"->"+str(right-1))
        return res