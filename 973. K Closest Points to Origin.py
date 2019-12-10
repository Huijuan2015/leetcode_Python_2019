class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        dist = [(point[0]*point[0]+ point[1]*point[1], point) for point in points]
        import heapq
        res = []
        heapq.heapify(dist)
        while K > 0:
            point = heapq.heappop(dist)
            res.append(point[1])
            K -= 1
        return res
    
            
        