class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0 # 记录你当前最远能跳到哪里
        for i in range(len(nums)):
            if i <= max_reach:
                max_reach = max(max_reach, nums[i]+i)
            else:
                return False
        return True


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0 # 记录你当前最远能跳到哪里
        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, nums[i]+i)
            if max_reach >= len(nums)-1:
                return True
        return False #逻辑不需要但程序需要