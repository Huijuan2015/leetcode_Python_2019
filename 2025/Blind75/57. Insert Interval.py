class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        # solution 1 stack
        
        if not intervals and not newInterval:
            return []
        intervals = sorted(intervals + [newInterval])
        stk = [intervals[0]]
        for interval in intervals[1:]:
            top = stk[-1]
            if interval[0] <= top[1]: #[3,6] [4,5]
                new = [top[0], max(top[1], interval[1])]
                stk.pop()
                stk.append(new)
            else:
                stk.append(interval)
        return stk


        # solution 2
        res = []
        start = newInterval[0]
        end = newInterval[1]
        # intervals: sorted already

        for i, interval in enumerate(intervals):
            if interval[1] < start: #[1,3] [4,5]
                res.append(interval)
            elif end < interval[0]:#[4,5] [1,3]
                res.append(newInterval)
                return res+intervals[i:]
            else:
                start = min(start, interval[0])
                end = max(end, interval[1])
                newInterval = [start, end]
        res.append(newInterval)
        return res


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
        intervals.sort()
        res = [intervals[0]]
        for interval in intervals[1:]:
            top  = res[-1]
            # [[1,2],[3,5],[4,8],[6,7],[8,10],[12,16]]
            # [[1,5], [6,9]]
            if top[1] < interval[0]:
                res.append(interval)
            elif top[1] >= interval[0]: #[1,5] [2,3] / [1,5] [1,3]
                new = [min(top[0], interval[0]), max(top[1], interval[1])]
                res.pop()
                res.append(new)
        return res


