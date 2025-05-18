class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height)-1
        res = 0
        while left < right:
            curr = min(height[left], height[right]) * (right-left)
            res = max(res, curr)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        res =  float('-inf')
        while left < right:
            curr = 0
            if height[left] <= height[right]:
                curr = height[left] * (right - left)
                left += 1
            else:
                curr = height[right] * (right - left)
                right -= 1
            res = max(res, curr)
        return res



