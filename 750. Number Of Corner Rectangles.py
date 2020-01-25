class Solution(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # m, n = len(grid), len(grid)
        count = collections.Counter()
        ans = 0
        for row in grid:
            for col1, val1 in enumerate(row):
                if val1:
                    for col2 in xrange(col1+1, len(row)):
                        if row[col2]:
                            print row, col1, col2, count,
                            ans += count[col1, col2]
                            print count
                            count[col1, col2] += 1
        # print count
        return ans
