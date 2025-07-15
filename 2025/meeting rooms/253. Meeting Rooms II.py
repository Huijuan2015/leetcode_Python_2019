class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
        if len(intervals) < 2:
            return len(intervals)
        starts, ends = [], []
        for start, end in intervals:
            starts.append(start)
            ends.append(end)
        starts.sort()
        ends.sort()
        available = rooms = 0
        i = j = 0
        while i < len(starts):
            if starts[i] < ends[j]:
                if available > 0:
                    available -= 1
                else:
                    rooms += 1
                i += 1
            else:
                available += 1
                j += 1
        return rooms





            

