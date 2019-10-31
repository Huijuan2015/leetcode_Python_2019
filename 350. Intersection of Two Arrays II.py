class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        mp = Counter(nums1)
        ans = []
        for num in nums2:
            if num in mp and mp[num] > 0:
                ans.append(num)
                mp[num] -= 1
            
        return ans