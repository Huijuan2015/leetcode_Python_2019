# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end = 1, n
        # 返回的start end是相连的2位，第二个肯定是bad
        while start+1 < end: # 考虑length 1的情况
            mid = start + (end-start)/2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid
        if isBadVersion(start):
            return start
        return end