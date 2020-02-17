class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
        intervals.sort()
        cnt = 0
        compare = intervals[0]
        # print intervals
        for interval in intervals[1:]: # remove大范围
            
            if interval[0] < compare[1]:
                cnt += 1
            if interval[1] <= compare[1] or interval[0] >= compare[1]:
                compare = interval
            
        return cnt
            
                
            