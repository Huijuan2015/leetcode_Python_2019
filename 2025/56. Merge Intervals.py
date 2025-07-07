class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        intervals.sort()
        for interval in intervals:
            if not res:
                res.append(interval)
            top = res[-1]
            if interval[0] <= top[1]:
                newInterval = [min(top[0], interval[0]), max(top[1], interval[1])]
                res.pop()
                res.append(newInterval)
            else:
                res.append(interval)
        return res
