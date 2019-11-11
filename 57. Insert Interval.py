class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        # stack
        if not intervals and not newInterval:
            return []
        intervals = sorted(intervals+[newInterval])
        stk = [intervals[0]]
        for interval in intervals[1:]:
            top = stk[-1]
            if interval[0] <= top[1]:
                new = [top[0], max(top[1], interval[1])]
                stk.pop()
                stk.append(new)
            else:
                stk.append(interval)
        return stk



        /////// O(N)
        res = []
        start = newInterval[0]
        end = newInterval[1]
        
        for i, interval in enumerate(intervals):
            # print interval, start, end
            if interval[1] < start:#完全在当前元素后
                res.append(interval)
            elif end < interval[0]:#完全在当前元素前
                res.append(newInterval)
                return res+intervals[i:]
            else: #一部分在当前内，一直更新可以插入的最大区间，不更新res
                start = min(start, interval[0])
                end = max(end, interval[1])
                newInterval = [start, end]
            # print res, start, end
        res.append(newInterval)            
        return res