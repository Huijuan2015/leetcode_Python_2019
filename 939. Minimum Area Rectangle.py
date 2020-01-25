class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # points.sort()
        seen = set()
        res = float('inf')
        for p1 in points:
            x1, y1 = p1
            for p2 in seen:
                x2, y2 = p2
                if (x1, y2) in seen and (x2, y1) in seen:
                    area = abs(x1-x2) *abs(y1-y2)
                    res = min(res, area)
            seen.add((x1,y1))
        # print seen
        return res if res!=float('inf') else 0