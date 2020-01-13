class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # subarray sum of k, new arr: len(nums)-k+1
        # leftSeen arr
        # rightSeen arr
        # sum of i, j, k: max sub sum in [0,j] + j + max sub sum in [j+1:]
        if not nums or len(nums) < k*3:
            return 
        subSum = [0 for _ in range(len(nums)-k+1)]
        #TLE
        # for i in range(len(nums)-k+1):
        #     subSum[i] = sum(nums[i:i+k])
        currSum = 0
        for i in range(len(nums)):
            currSum += nums[i]
            if i >= k:
                currSum -= nums[i-k]
            if i >= k-1:
                subSum[i-k+1] = currSum
                            
        n = len(subSum)
        leftSeen, rightSeen = [0 for _ in range(n)], [n-1 for _ in range(n)]
        for i in range(1, n): # indexes
            leftSeen[i] = i if subSum[i] > subSum[leftSeen[i-1]] else leftSeen[i-1]
        for i in range(n-2, -1, -1): # indexes
            rightSeen[i] = i if subSum[i] >= subSum[rightSeen[i+1]] else rightSeen[i+1]
        maxSum = float('-inf')
        res = [-1,-1,-1]
        for second in range(k, n-k):
            first = leftSeen[second-k]
            third = rightSeen[second+k]
            curr = subSum[first] + subSum[second] + subSum[third]
            if maxSum < curr:
                res = [first, second, third]
                maxSum = curr
        return res
            