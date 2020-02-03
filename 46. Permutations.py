class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        visited = set()
        self.findPath(nums, visited, [])
        return self.res
    
    def findPath(self, nums, visited, path):
        if len(path) == len(nums):
            self.res.append(path)
            return
        for num in nums:
            if num not in visited:
                visited.add(num)
                self.findPath(nums, visited, path+[num])
                visited.remove(num)

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


            就是一个线程负责某个数字开头的permutation