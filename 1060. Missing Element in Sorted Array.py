class Solution(object):
    def missingElement(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        missing = [nums[i]-nums[0]-i for i in range(len(nums))]
        # print missing
        start, end = 0, len(nums)-1
        if k > missing[-1]:
            return nums[-1] + k-missing[-1]
        while start < end:
            mid = (start+end)//2
            #找到有k个missing的index-> start
            if missing[mid] < k:
                start = mid+1
            else:
                end = mid
        print start, end
        # i = min(start, end)
        return nums[start-1]+k-missing[start-1]
        # missing[start]: 第一个大于k的数
        # 结果：start前一位 + (start-1位之前missing的数)
            
            
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