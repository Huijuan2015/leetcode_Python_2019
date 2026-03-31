class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        for interval in intervals[1:]:
            last = res[-1]
            if last[1] >= interval[0]:
                new = [last[0], max(last[1], interval[1])]
                res[-1] = new
            else:
                res.append(interval)
        return res
            

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals.sort()
        # 避免不必要的次要排序：如果两个区间的 start 相同，
        # intervals.sort() 会去比较 end；
        # 而 key=lambda x: x[0] 则认为它们相等。
        # 在某些极端数据下，减少比较维度反而能省时。
        intervals.sort(key=lambda x: x[0]) 
        res = []

        for interval in intervals:

            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                new = [res[-1][0], max(res[-1][1], interval[1])]
                res[-1] = new
        return res
            

