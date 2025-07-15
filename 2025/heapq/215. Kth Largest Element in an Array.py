class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # heapq # kth largest,  保留重复
        # 一直只保留最大的 k 个数（通过删除小的），最后堆顶是这组里最小的，也就是 第 k 大的数。
        import heapq
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]