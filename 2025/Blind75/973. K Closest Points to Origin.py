class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        dist = [(point[0]*point[0] + point[1]*point[1], point) for point in points]
        import heapq
        heapq.heapify(dist)
        res = []
        while k > 0:
            point = heapq.heappop(dist)
            res.append(point[1])
            k -= 1
        return res

