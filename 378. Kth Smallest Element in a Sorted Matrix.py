class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        def smallerThan(x):
            i, j = n - 1, 0
            cnt = 0
            while i >= 0 and j < n:
                if matrix[i][j] > x:
                    i -= 1
                else:
                    j += 1
                    cnt += i + 1
            return cnt
        lo, hi = matrix[0][0], matrix[n - 1][n - 1]
        while lo < hi:
            mi = (hi - lo) // 2 + lo
            if smallerThan(mi) < k:
                lo = mi + 1
            else: 
                hi = mi
        return lo



        使用二分法初始将left取最小值, right取最大值，然后每次扫描整个数组查找小于(left+right)/2的元素个数，
        如果此个数小于k，则将left值变为mid+1，否则right = mid，这样的时间复杂为log(Max-Min)*n*log(n)，
        相比与上题来说这种算法依赖与数组中的最大值和最小值的差，不过对于大的数据来说其表现还是优于上个算法．
