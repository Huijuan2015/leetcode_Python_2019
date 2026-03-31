class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0
        for num in num_set:
            if num-1 not in num_set: #阶段最小
                n = num
                curr_count = 1
                while n+1 in num_set:
                    curr_count += 1
                    n += 1
                res =  max(res, curr_count)
        return res