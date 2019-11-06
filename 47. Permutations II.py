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
            
                