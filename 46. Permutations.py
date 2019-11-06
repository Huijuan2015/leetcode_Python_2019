class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        visited = [False] * len(nums)
        self.helper(nums, visited, [])
        return self.res
    
    def helper(self, nums, visited, path):
        if len(path) == len(nums):
            self.res.append(path)
            return
        for idx in range(len(nums)):
            if visited[idx]: continue
            visited[idx] = True
            self.helper(nums, visited, path+[nums[idx]])
            visited[idx] = False