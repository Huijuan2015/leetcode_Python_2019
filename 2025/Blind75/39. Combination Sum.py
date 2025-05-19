class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        def dfs(start, currSum, path):
            if currSum == target:
                res.append(list(path)) #  path 是一个可变的列表对象（list），在回溯算法中它会不停地被修改（添加和删除元素）
            if currSum > target:
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                dfs(i, currSum+candidates[i], path)
                path.pop()
        dfs(0, 0, [])
        return res

        