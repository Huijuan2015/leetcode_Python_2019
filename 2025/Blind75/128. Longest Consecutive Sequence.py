class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums)
        res = 0
        for num in numSet: # 只需要边里set里的数
            #只有num-1不存在时，才开始新的查找
            if num-1 not in numSet:
                cnt = 1
                curr = num
                while curr+1 in numSet:
                    cnt += 1
                    curr += 1
                res = max(cnt, res)
        return res
