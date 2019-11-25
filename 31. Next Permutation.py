class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                k = i
                break

        if k == -1:
            return nums.sort()
        l = -1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] > nums[k]:
                l = i
                break

        nums[k], nums[l] = nums[l], nums[k]

        k += 1
        l = len(nums)-1
        while k < l:
            nums[k], nums[l] = nums[l], nums[k]
            k +=1
            l -= 1
        return nums


[1,2,7,4,3,1] ====> [1,3,1,2,4,7]
规律就是说 从后向前遍历，找到第一个降序的数字，2。
然后继续从后向前遍历，找比这个数大的第一个数，3。
之后交换两个数字，变成 [1,3,7,4,2,1]
然后把后面的数字 反转，变成 [1,3,1,2,4,7] 即为最终答案。

