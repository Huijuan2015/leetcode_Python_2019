class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        # no intervals
        if not intervals or len(intervals)<2:
            return True
        intervals.sort()
        for i in range(len(intervals)-1):
            #i, i+1
            if intervals[i+1][0] < intervals[i][1]:
                return False
        return True