class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        nums.sort()
        visited = set()
        self.findPath(nums, [], 0, visited)
        return self.res
    
    def findPath(self, nums, path, idx, visited):
        if idx == len(nums):
            self.res.append(path)
            return
        #not add
        self.findPath(nums, path, idx+1, visited)
        # try add
        if idx not in visited:
            if idx-1>=0 and nums[idx] == nums[idx-1] and idx-1 not in visited:
                return
            visited.add(idx)
            self.findPath(nums, path+[nums[idx]], idx+1, visited)
            visited.remove(idx)
        
        

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