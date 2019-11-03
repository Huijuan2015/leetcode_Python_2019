class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        followup是如何把它的复杂度降到o(nk), 那么就是如果将颜色的部分只扫一遍。参考leetcode的discuss里most voted answer, 只需要记录下每个house的最小的两个颜色。如果下一个颜色跟这个颜色不一样，就取最小的这个颜色加上这次所选的颜色，并找出最小值；如果下一个颜色跟这个颜色一样，那么我们不可以取最小的这个颜色，所以我们取第二小的颜色加上这次所选的颜色。最后把最小的颜色输出就可以了。
        if not costs:
            return 0
        n, k = len(costs), len(costs[0])
        for i in range(1,n):
            min1 = min(costs[i-1])
            idx = costs[i-1].index(min1)
            min2 = min(costs[i-1][:idx]+costs[i-1][idx+1:])
            for j in range(k):
                if j == idx:
                    costs[i][j] += min2
                else:
                    costs[i][j] += min1
        return min(costs[-1])