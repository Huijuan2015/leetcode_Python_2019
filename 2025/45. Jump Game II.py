greedy O(n)
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    #     • end：当前这一步能跳到的最远位置（跳跃边界）。
    # • farthest：在当前边界内，我们能跳到的最远位置（下一步的边界）。
        jumps = 0
        end = 0
        farthest = 0

        for i in range(len(nums)-1):
            farthest = max(farthest, i +nums[i])
            if i == end:
                jumps += 1
                end = farthest

        return jumps


DP O(n2)
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp[i] min step jump to index i
        # i+nums[i] : min(dp[i],  dp[i] + 1) 
        dp = [float('inf')] * len(nums)
        dp[0] = 0 # 起点不需要跳跃
        for i in range(len(nums)):
            end = min(len(nums), i +nums[i]+1)
            for j in range(i+1, end):
                dp[j] = min(dp[j], dp[i] + 1)
        # print dp
        return dp[-1]
        
