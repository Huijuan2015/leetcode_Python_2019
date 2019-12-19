Time complexity : O(m*n). The whole numsnums array, of length nn needs to be scanned for all the mm elements of finalNumsfinalNums in the worst case.

Space complexity : O(m)

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        mp = {num:idx for idx, num in enumerate(nums2)}
        res = [-1 for _ in range(len(nums1))]
        for i, num in enumerate(nums1):
            j = mp[num]
            for j in range(j+1, len(nums2)):
                if nums2[j] > num:
                    res[i] = nums2[j]
                    break
        return res

Time complexity : O(m+n). The entire numsnums array(of size nn) is scanned only once. The stack's nn elements are popped only once. The findNumsfindNums array is also scanned only once.

Space complexity : O(m+n). stack
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        mp = {}
        stk = []
        res = []
        for num in nums2:
            if stk and stk[-1] < num:
                while stk and stk[-1] < num:
                    mp[stk.pop()] = num
            stk.append(num)
                
        while stk:
            mp[stk.pop()] = -1
        for num in nums1:
            res.append(mp[num])
        return res
        