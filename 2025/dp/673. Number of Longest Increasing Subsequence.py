class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 下标可以不连续，但值要递增
        if len(nums) <= 1:
            return len(nums)
        # •	length[i]: 以 nums[i] 结尾的最长递增子序列的长度
	    # •	count[i]: 以 nums[i] 结尾的最长递增子序列的 个数

        length = [1 for _ in range(len(nums))]
        count = [1 for _ in range(len(nums))]

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = count[j]
                    elif length[j] + 1 == length[i]:
                        count[i] += count[j]
        max_len = max(length)
        return sum(c for i, c in enumerate(count) if length[i] == max_len)
    
                    





