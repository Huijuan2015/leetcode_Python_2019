class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, high, curr = 0, len(nums)-1, 0
        while curr <= high:
            if nums[curr] == 2:
                nums[curr], nums[high] = nums[high], nums[curr]
                high -= 1
            elif nums[curr] == 0:
                nums[curr], nums[low] = nums[low], nums[curr]
                low += 1
                curr += 1 # 换回来的只可能是 1，所以 curr 可以前进
            else:
                curr += 1   
            

