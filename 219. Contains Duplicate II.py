class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        indexMap = {}
        for i,n in enumerate(nums):
            # print (n,i)
            if not indexMap.has_key(n):
                indexMap[n] = i
            else:
                if i - indexMap[n] <= k:
                    return True
                else:
                    indexMap[n] = i
        return False
        