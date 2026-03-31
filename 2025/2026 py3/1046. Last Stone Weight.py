class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 最大堆
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            first = heapq.heappop(max_heap)
            second = heapq.heappop(max_heap)
            if first != second:
                heapq.heappush(max_heap, first - second)
        return -heapq.heappop(max_heap) if max_heap else 0