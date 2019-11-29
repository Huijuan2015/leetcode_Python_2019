class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import defaultdict
        if not nums:
            return 0
        mp = defaultdict(int)
        mp[0] = 1
        cnt = 0
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum-k in mp:
                cnt += mp[sum-k]
            mp[sum] += 1
        # print sum
        return cnt
        
        
            
            
        