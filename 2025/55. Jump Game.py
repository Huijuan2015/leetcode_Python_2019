class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 维护一个变量 farthest，记录当前能够跳到的最远位置。遍历数组，更新这个最远距离。如果在某个位置 i 时，发现 i > farthest，说明跳不到这个位置，返回 False。否则，如果 farthest >= len(nums) - 1，说明可以跳到或超过最后一位，返回 True。
        farthest = 0
        for i in range(len(nums)):
            if i > farthest:
                return False
            farthest = max(farthest, i + nums[i])
        return True
        