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

