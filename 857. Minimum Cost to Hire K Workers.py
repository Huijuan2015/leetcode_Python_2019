class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        workers = []
        for i in range(len(quality)):
            q, w = quality[i], wage[i]
            workers.append([float(w)/q, w, q])
        res = float('inf') #lease money
        workers.sort()
        # print workers
        pool = []
        sumq = 0
        for ratio, w, q in workers: # 在当前ratio下，拿到最小的quality
            heapq.heappush(pool, -q)
            sumq += q
            # print ratio, pool, len(pool), K
            if len(pool) > K:
                sumq += heapq.heappop(pool) # pop 出quality最多的一个
            if len(pool) == K:
                res = min(res, ratio*sumq)
        return float(res)