class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return 
        nums.sort()
        visited = set() #放 index
        self.res = []
        self.findPath(nums, visited, [])
        return self.res
    
    def findPath(self, nums, visited, path):
        if len(path) == len(nums):
            self.res.append(path)
            return
        for i, num in enumerate(nums):
            if i-1 >= 0 and nums[i] == nums[i-1] and i-1 not in visited:
                continue
            if i not in visited:
                visited.add(i)
                self.findPath(nums, visited, path+[num])
                visited.remove(i)

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        visited = [False] * len(nums)
        self.res = []
        self.helper(nums, visited, [])
        return self.res
    
    def helper(self, nums, visited, path):

        if len(nums) == len(path):
            self.res.append(path)
            return
        for i in range(len(nums)):
            # print path
            if visited[i]: continue
                # 只有在第1个1用过的情况下，才可以使用第二个1； 如果第一个1没被用过，则跳过
            if i -1 >= 0 and not visited[i-1] and nums[i] == nums[i-1]: continue
            visited[i] = True
            self.helper(nums, visited, path+[nums[i]])
            visited[i] = False
            
                