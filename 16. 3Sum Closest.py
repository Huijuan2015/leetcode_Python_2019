class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # unsorted: sort (nlgn) + 2 pointers
        # unsorted: map S:O(n) T:O(n)
        nums.sort()
        res = nums[0]+nums[1]+nums[2]
        
        for i in xrange(len(nums)-2):
            start = i+1
            end = len(nums)-1
            while start < end:
                tmp = nums[i] + nums[start]+nums[end]
                if abs(tmp-target) < abs(res-target):
                    res = tmp
                if tmp < target:
                    start += 1
                else:
                    end -= 1
        return res