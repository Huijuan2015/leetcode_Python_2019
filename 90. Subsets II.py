class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        self.res = []
        self.helper(nums, 0, [])
        return self.res
    
    def helper(self, nums, start, path): #找当前start开始的子集
        self.res.append(path)#不加任何元素
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            self.helper(nums, i+1,path+[nums[i]])#子集， 添加新元素