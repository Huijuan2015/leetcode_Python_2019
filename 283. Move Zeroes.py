class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        first, second = 0, 0
        while second < len(nums):
            if nums[second] != 0: # curr 不等于0， first往前走; curr=0, first 就停下来
                nums[first], nums[second] = nums[second], nums[first]
                first += 1 #first一直在第一个0上
            second += 1
                
            