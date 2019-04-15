class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        #I used hash set and it's O(1) to check if it contains an element.
        #So the total time complexity will be O(M+N), instead of O(MN)
        setJ = set(J)
        #return sum(s in setJ for s in S)
        res = 0
        for s in S:
            if s in setJ:
                res += 1
        return res
        