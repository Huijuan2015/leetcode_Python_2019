class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(numbers)-1
        while start < end:
            if numbers[start]+numbers[end] == target:
                return [start+1, end+1]
            while numbers[start]+numbers[end] < target and start < end:
                start += 1
            while numbers[start]+numbers[end] > target and start < end:
                end -= 1
            
            