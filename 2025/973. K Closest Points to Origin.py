class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        #维持k长度最小堆，距离用负数， 有比堆顶大的就PUSH，长度超过K就 POP
        min_heap = []
        for point in points:
            x, y = point[0], point[1]
            dist = -1 * (x*x + y*y)
            if not min_heap or len(min_heap) < k:
                heapq.heappush(min_heap, (dist, point))
            else:
                if min_heap[0][0] < dist:
                    heapq.heappush(min_heap, (dist, point))
                    heapq.heappop(min_heap)
        res = []
        for pair in min_heap:
            res.append(pair[1])
        return res
                


            