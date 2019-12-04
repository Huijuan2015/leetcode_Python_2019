总结：
要回头，有重复 所以要visited

subsets:
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
            
permutation
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        # for i in range(len(nums)):
        visited = [False for _ in range(len(nums))]
        self.findPath(nums, [], visited)
        return self.res
    
    def findPath(self, nums, path, visited):
        if len(path) == len(nums):
            self.res.append(path)
            return
        
        for i in range(len(nums)):
            if not visited[i]:
                visited[i] = True
                self.findPath(nums, path+[nums[i]], visited)
                visited[i] = False
                
subsets II
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

permutation II
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
            
