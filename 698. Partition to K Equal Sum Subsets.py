class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # sum(nums)/k, dp[i]能否取出数 sum为i
        target = sum(nums)/k
        if sum(nums)%k!= 0:
            return False
        
        #k个sum
        subSums = [0 for _ in range(k)]
        nums.sort()
        return self.dfs(nums, target, subSums, len(nums)-1)
     # 我们用一个变量idx表示当前遍历的数字，排序后，我们从末尾大的数字开始累加，
     # 我们遍历数组v，当前位置加上nums[idx]，如果超过了target，我们掉过继续到下一个位置，]
     #    否则就调用递归，此时的idx为idx-1，表示之前那个数字已经成功加入数组v了，我们尝试着加下一个数字。
     #    如果递归返回false了，我们就将nums[idx]从数组v中对应的位置减去，还原状态，然后继续下一个位置。
     #    如果某个递归中idx等于-1了，表明所有的数字已经遍历完了，此时我们检查数组v中k个数字是否都为target，是的话返回true，否则返回false，   
    def dfs(self, nums, target, subSums, idx):# 从最后一位开始是否是得到k个target
        if idx == -1:
            for s in subSums:
                if s != target:
                    return False
            return True
        num = nums[idx]
        for i in range(len(subSums)):
            if subSums[i] + num > target:
                continue
            subSums[i] += num
            if self.dfs(nums, target, subSums, idx-1):
                return True
            subSums[i] -= num
        return False
