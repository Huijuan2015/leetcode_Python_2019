class Solution(object):
    def missingElement(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        missing = [nums[idx]-nums[0]-idx for idx in range(len(nums))]
        # print missing
        n = len(nums)
        if k > missing[-1]:
            return nums[-1] + k-missing[-1]
        
        start, end = 0, n-1
        while start != end:
            pivot = (start+end)//2
            if missing[pivot] < k:
                start = pivot+1
            else:
                end = pivot
        return nums[start-1]+k-missing[start-1]


class Solution(object):
    def missingElement(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        missing = [nums[idx]-nums[0]-idx for idx in range(len(nums))]
        # print missing
        n = len(nums)
        if k > missing[-1]:
            return nums[-1] + k-missing[-1]
        idx = 1
        while missing[idx] < k:
            idx += 1
        return nums[idx-1]+k-missing[idx-1]