class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        # 要记住index, 来计算前面所有可能，比如[2，1，2] => return 3
        heights.append(0)
        stk = [-1]
        res = 0
        for i in range(len(heights)):
            while heights[i] < heights[stk[-1]]:
                lastHeight = stk.pop()
                width = i-stk[-1]-1
                res = max(res, lastHeight*width)
            stk.append(i)
        heights.pop() #还原heights..
        return res

Simple Divide and Conquer AC solution without Segment Tree
https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/28941/Segment-tree-solution-just-another-idea-O(N*logN)-Solution