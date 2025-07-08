class Solution(object):
    def findBuildings(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        tallest = 0
        res = []
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > tallest:
                res.append(i)
            tallest = max(tallest, heights[i])
        # res.sort()
        # return res
        return res[::-1] #空间 O(n)， 时间 O(n)
            