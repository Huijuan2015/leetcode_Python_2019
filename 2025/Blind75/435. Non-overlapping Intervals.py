class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals or len(intervals) < 2:
            return 0
        res = 0
        intervals.sort(key = lambda x: x[1])
        # print intervals
    
    # 1.    按照 区间的结束时间从小到大排序。(贪心算法的核心策略)
    # 2.    遍历每个区间，用一个变量 end 记录上一个被保留的区间的结束时间。
    # 3.    如果当前区间的开始时间 < end，说明和上一个区间重叠了，必须移除一个，计数器 +1。
    # 4.    否则，更新 end = 当前区间的结束时间。
        end = float('-inf')
        for interval in intervals:
            if interval[0] < end:
                res += 1
            else:
                end = interval[1]
        return res
         



class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # solution 1
        # （贪心策略）如果发生重叠，就移除结束时间较晚的区间，
        # 因为在按起始时间升序排列的数组中，结束时间较晚的区间更容易与后续区间产生更多重叠
        if not intervals:
            return0
        intervals.sort()
        cnt = 0
        compare = intervals[0]
        # [[1,10], [2,3], [3,4], [5,6]]
        for interval in intervals[1:]:
            if interval[0] < compare[1]: #[1,10], [2,3] remove large one [1,10]
                cnt += 1
            if interval[1] <= compare[1] or interval[0] >= compare[1]:
                # 换成小interval
                compare = interval
        return cnt



        # solution 2
        # 将区间按结束时间排序
        # 如果我们按结束时间排序，一旦发生重叠，后出现的区间一定是要被移除的那个（因为它的结束时间更大，会带来更多重叠）。
        # [[2,3], [3,4], [5,6], [1,10], [6,11], [9,12]]
        # 省略步骤：比较 [5,6] 和 [1,10] 时，可以直接移除后者 [1,10]，因为它的结束时间更大，
        # 会在后续与 [6,11] 和 [9,12] 等区间产生更多重叠。

        intervals.sort(key=lambda x:x[1])
        prev = float('-inf')
        ans = 0
        for i in intervals:
            if i[0] >= prev:
                prev = i[1]
            else:
                ans += 1
        return ans

