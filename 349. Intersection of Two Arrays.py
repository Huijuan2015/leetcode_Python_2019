class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # 1. brute force O(n^2), ? O(n)
        ans = set()
        # for num1 in nums1:
        #     for num2 in nums2:
        #         if num2 == num1:
        #             ans.add(num2)
        # return ans
        
        # 2. map space O(n), time O(n)
        mp = {u:i for i, u in enumerate(nums1)}
        
        for num in nums2:
            if num in mp:
                ans.add(num)
        return ans
        
        #3. 2 pointers for 2 list  nlgn
        # 2个指针分别向前走，相等就放入return
        
        # master python code
        nums1=set(nums1)
        nums2=set(nums2)
        return list(nums1&nums2)
    
        intersection = lambda *p: list(set(p[1]) & set(p[2]))