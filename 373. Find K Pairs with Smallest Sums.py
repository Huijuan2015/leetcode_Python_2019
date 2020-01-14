class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2:
            return []
        # 先把(A[i], B[0]) 所有 pair 推进pq (sum, i, j)
        # pq每次pop(A[i],B[j])出来，就把A[i], B[j+1]推进去 (sum, i, j+1)
        arr = []
        for i in range(len(nums1)):
            arr.append((nums1[i]+nums2[0], i, 0))
        heapq.heapify(arr)
        res = []
        while k>0 and arr:
            sum, i, j = heapq.heappop(arr)
            res.append([nums1[i], nums2[j]])
            if j+1 < len(nums2):
                heapq.heappush(arr, ((nums1[i]+nums2[j+1]), i, j+1))
            k -= 1
        return res
        

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        # m*n
        if not nums1 or not nums2:
            return []
        arr = []
        for num1 in nums1:
            for num2 in nums2:
                arr.append((num1+num2, [num1, num2]))
        heapq.heapify(arr)
        res = []
        while k > 0 and arr:
            res.append(heapq.heappop(arr)[1])
            k -= 1
        return res
        