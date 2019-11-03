class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # (y2-y1)/(x2-x1) = (y3-y1)/(x3-x1)
        # 但是我们要让这两数分别除以它们的最大公约数，这样例如8和4，4和2，2和1
        import collections
        if len(points) <= 2:
            return len(points)
        
        # 最大公约数 greatest common divisor
        def getgcd(a, b):
            return getgcd(b%a, a) if a!= 0 else b
        
        ans = 0
        d = collections.defaultdict(int)
        
        for i in range(len(points)):
            d.clear()
            overlap = 0
            curmax = 0
            # 与当前点可以在同一条线上可能有多少点：重合的点+k相同的点+本身
            for j in range(i + 1, len(points)):
                dex = points[j][0] - points[i][0]
                dey = points[j][1] - points[i][1]
                gcd = getgcd(dex, dey)
                if dex == 0 and dey == 0: #点重合
                    overlap += 1
                    continue
                d[(dey//gcd, dex//gcd)] += 1
                curmax =  max(curmax, d[(dey//gcd, dex//gcd)])
            ans = max(ans, curmax+overlap+1)
        return ans

        