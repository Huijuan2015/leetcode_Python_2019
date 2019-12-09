维持左右两边指针，1>要确保两个指针移动
2>计算：比当前小，就计算
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right, leftMax, rightMax, res = 0, len(height)-1, 0, 0, 0
        while left < right:
            # left < right, left ++
                # if  smaller, res += (leftMax - curr)
                # if bigger, leftMax = curr
            # else, right --
                # if smaller, res += rightMax-curr
                #if bigger, rightMax = curr
            if height[left] <= height[right]:
                while left < right and height[left] <= leftMax:
                    res += leftMax - height[left]
                    left += 1
                leftMax = height[left]
            else:
                while left < right and height[right] <= rightMax:
                    res += rightMax - height[right]
                    right -= 1
                rightMax = height[right]      
        return res

其实不需要维持rightmax， leftMax
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right,res = 0, len(height)-1, 0
        while left < right:
            if height[left] <= height[right]: 这两种条件都可，只要确保左右指针会移动
            #if leftMax <= rightMax
                leftMax =  height[left]
                while left < right and height[left] <= leftMax:
                    res += leftMax - height[left]
                    left += 1
            else:
                rightMax = height[right]
                while left < right and height[right] <= rightMax:
                    res += rightMax - height[right]
                    right -= 1
        return res