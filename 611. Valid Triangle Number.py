class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #2 pointer, sort,
        nums.sort()
        res = 0
        # 不需要去重
        for third in range(2, len(nums)):
            if nums[third] == 0:
                continue
            # if third+1 < len(nums) and nums[third] == nums[third+1]:
            #     continue
            first = 0
            second = third-1
            while first < second:
                if nums[second] == 0:
                    break 
                if nums[first] == 0:
                    first += 1
                    continue
                 
                if nums[first] + nums[second] <= nums[third]:
                    first+=1
                else:
                    res += (second-first)
                    # print nums[first], nums[second], nums[third]
                    # while second-1 > 0 and nums[second-1] == nums[second]:
                    #     second -= 1
                    second -= 1
        return res        
                
        # 不用 sort, recursive, TLE
#         self.res = 0
#         self.helper(0, nums,[])
#         return self.res
    
#     def helper(self, idx, nums, path):
#         if len(path) == 3:
#             path.sort()
#             if path[0] +path[1]>path[2]:
#                 print path
#                 self.res += 1
#             return
#         for i in range(idx, len(nums)):
#             self.helper(i+1, nums, path+[nums[i]])

        