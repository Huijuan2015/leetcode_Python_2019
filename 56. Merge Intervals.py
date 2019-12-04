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
            if last[1] >=interval[0]:
                res[-1] = [min(last[0], interval[0]), max(last[1], interval[1])]
            else:
                res.append(interval)
        return res

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        if not intervals:
            return 
        prev = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if curr[0] <= prev[1]:
                prev = [min(prev[0], curr[0]), max(prev[1],curr[1])]
            else:
                res.append(prev)
                prev = curr
        res.append(prev) 
        return res
            


    