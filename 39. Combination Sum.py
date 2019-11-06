class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.helper(candidates,target,[], 0)
        return self.res
    dfs    
    def helper(self, candidates, target, tmp, index):
        if target < 0:
            return
        if target == 0:
            # print temp
            # cur = tmp[:]
            self.res.append(tmp)
            print self.res
            return
        for i in range(index, len(candidates)):
            c = candidates[i]

            self.helper(candidates, target-c, tmp+[c], i)

dp

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> int:
        # 保存方案，使用三维数组
        # 第一维： dp:List 表示和为不同数时的方案
        # 第二维： dp[s]:List 表示和i的方案列表
        # 第三维 每种具体的方案都是数组， dp[s][j]:List 表示和为s的第j个方案的数组
        dp: list = [[[]]] + [[] for i in range(target)]  # 初始化 eg: [[[]], [], [], [], [], []]， 保证和为0有一种方案 [], 完全背包需要恰好装满的时候，dp[0] 必须初始化为0

        for n in nums:  # 对于每个数
            for s in range(n, target + 1):  # 完全背包，从小到大
                li = [l + [n] for l in dp[s - n]]  # 对于把和为s-n的每种方案，添加数字n, 就变成一种新的 和为s的方案
                dp[s] += li  # 把新方案添加到 原来和为s的方案里
        return dp[target]