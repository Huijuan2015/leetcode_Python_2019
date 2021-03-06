class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        subSum = collections.defaultdict(int)
        curr = 0
        res = 0
        subSum[0] = 1
        for i in range(len(nums)):
            curr += nums[i]
            if subSum[curr-k]:
                res += subSum[curr-k]
            subSum[curr] += 1
        # print subSum
        return res

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        前缀和相减
        import collections
        mp = collections.defaultdict(int) #sum:same sum count
        sum = 0
        cnt = 0
        mp[0] = 1
        for i in range(len(nums)):
            sum += nums[i]
            if sum-k in mp:
                cnt += mp[sum-k]
            mp[sum] += 1
        return cnt

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
        
        
            
            
        