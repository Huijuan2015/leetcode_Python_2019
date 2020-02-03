class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # dp[i] 原数组能不能取出若干使得和为i

        target = sum(nums)/2
        if sum(nums)%2 != 0:
            return False
        dp = [False for _ in range(target+1)]
        dp[0] = True
        for num in nums: #s[i-1]
            for j in range(target, num-1, -1): #要倒序 33345： 第一轮3， 标记dp[3]; 第二轮3， 标记dp[6]; 第三轮3，标记dp[9]...
                dp[j] = dp[j] or dp[j-num]
                print num, j, dp
        print dp
        return dp[-1]
                    
        # wrong
        #  找到组成half sum的数
#         nums.sort()
#         target = sum(nums)/2
#         if sum(nums)%2 != 0:
#             return False
#         i, j = 0, 0
#         print nums, sum(nums)
#         while j < len(nums):
#             print i, j, target
#             if target == 0:
#                 return True
#             elif target > 0:
#                 target -= nums[j]
#                 j+=1
#             else:
#                 target += nums[i]
#                 i += 1
            
#         return False     
 
        
                
       
        
        
        