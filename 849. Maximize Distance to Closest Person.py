class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        res, curr = 0, 0
        # seats = [0]+seats+[0]
        for i in range(len(seats)):
            if seats[i] == 0:
                curr += 1
                if curr == i+1 or i == len(seats)-1: 开头 末尾
                    res = max(res, curr)
                else:
                    res = max(res, (curr+1)//2)
                
            else:
                curr = 0
        return res