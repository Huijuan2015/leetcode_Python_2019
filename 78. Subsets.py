class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        self.helper(nums, 0, [])
        return self.res
    
    def helper(self, nums, start, path):
        self.res.append(path)
        for i in range(start, len(nums)):
            # path.append(nums[i])
            self.helper(nums, i+1, path+[nums[i]])
            # path.pop()
            
            