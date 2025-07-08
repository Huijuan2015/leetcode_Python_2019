class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None, modifies nums in-place
        """
        n = len(nums)
        i = n - 2

        # 第一步：找到第一个下降的位置 i
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # 第二步：从右往左找到第一个比 nums[i] 大的数
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # 交换 i 和 j
            nums[i], nums[j] = nums[j], nums[i]

        # 第三步：反转 i+1 到末尾的部分
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1