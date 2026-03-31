class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        set1 = set(nums1)
        res = set()
        for num in nums2:
            if num in set1:
                res.add(num)
        return list(res)



class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #双指针，排序 然后查找
        res = []
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] ==  nums2[j]:
                if not res or nums1[i] != res[-1]:
                    res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] <  nums2[j]:
                i += 1
            else:
                j += 1
        return res