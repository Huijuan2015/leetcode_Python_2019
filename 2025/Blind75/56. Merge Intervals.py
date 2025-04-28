class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals or len(intervals) <= 1:
            return intervals
        intervals.sort()
        res = [intervals[0]]
        for interval in intervals[1:]:
            last = res[-1]
            if last[1] >= interval[0]:#[2,6],[4,10]
                res[-1] = [min(last[0], interval[0]), max(last[1], interval[1])]
            else:
                res.append(interval)
        return res




