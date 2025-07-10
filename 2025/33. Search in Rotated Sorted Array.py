class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #有序段
        left, right = 0, len(nums) - 1
        while left <= right: #找target要等于
            mid = (left+right)//2
            if nums[mid] ==  target:
                return mid
            if nums[mid] >= nums[left]: # 左边有序段
                # nums = [4, 5, 6, 7, 0, 1, 2]
                #     target = 0
                # mid = 3, nums[mid]=7
                # •	target=0 <= 7 成立
                # •	但实际上 0 根本不在 [4,5,6,7] 这段有序区间中
                if nums[left] <= target < nums[mid]:
                    # 二分查找时，必须收缩搜索区间，否则当 left == mid 或 right == mid 时，下一轮仍然是相同的范围，会无限循环。
                    # target  == nums[mid] 的情况已经在上面被找到了
                    right = mid - 1
                else:
                    left =  mid + 1
            else: # 右边有序段
                if nums[right] >= target > nums[mid]:
                    left = mid + 1
                else:
                    right  = mid - 1
        return -1
