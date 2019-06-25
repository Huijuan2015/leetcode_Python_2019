class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in xrange(len(nums)):
            target = -nums[i]
            start = i+1
            end = len(nums)-1

            if i-1 >= 0 and nums[i] == nums[i-1]:
                continue
            while start < end:
                first = nums[i]
                second = nums[start]
                third = nums[end]
                if second + third < target and start < end:
                    start += 1
                elif second + third > target and start < end:
                    end -= 1
                if second + third == target:
                    res.append([first,second,third])
                    while start < end and nums[start] == second:
                        start += 1
                    while start < end and nums[end] == third:
                        end -= 1      
        return res