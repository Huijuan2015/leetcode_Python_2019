class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums or len(nums) < 2:
            return nums
        pivot = len(nums)//2
        l = self.sortArray(nums[:pivot])
        r = self.sortArray(nums[pivot:])
        return self.sort2(l,r)
        
        
    def sort2(self, l, r):
        i, j = 0, 0
        res = []
        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                res.append(l[i])
                i += 1
            else:
                res.append(r[j])
                j += 1
        res.extend(l[i:])
        res.extend(r[j:])
        return res
        