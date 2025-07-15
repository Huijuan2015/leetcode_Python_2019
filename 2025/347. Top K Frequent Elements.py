class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count_map = Counter(nums)
        #heapq 
        #  (1, 3 ), (2, 2), (3, 1)
        #  top k 维持一个K的heapq
        queue = []
        for num, count in count_map.items():
            heapq.heappush(queue, (count, num))
            if len(queue) > k:
                heapq.heappop(queue)
        res = []
        for pair in queue:
            res.append(pair[1])
        return res
            
         
