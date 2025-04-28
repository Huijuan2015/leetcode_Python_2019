class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # count intervals
        starts, ends = [], []
        for interval in intervals:
            starts.append(interval[0])
            ends.append(interval[1])
        starts.sort()
        ends.sort()
        available = 0 
        i, j, cnt = 0, 0, 0
        #[0, 2, 5, 15]
        #[3, 10, 20, 30]
        while i < len(starts):
            if starts[i] < ends[j]:
                if available > 0:
                    available -= 1
                else:
                    cnt += 1
                i += 1
            else:
                available += 1
                j += 1
        return cnt
