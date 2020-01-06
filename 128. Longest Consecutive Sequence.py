class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # set
        # O(n),O(n)

        s = set(nums)
        res = 0
        for num in nums:
            tmp = 1
            if num-1 not in s: 只有num-1不存在时，才开始新的查找
                n = num
                while n+1 in s:
                    n += 1
                    tmp += 1
            res = max(tmp, res)
        return res
            
"""       
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #no sort
        #val: index
        visitDict = {x:False for x in nums} #val: if visited
        res = 0
        for i in visitDict:
            if visitDict[i] == False:
                curr = i+1
                lenRight = 0
                while curr in visitDict:
                    lenRight += 1
                    visitDict[curr] = True
                    curr += 1
                curr = i-1
                lenLeft = 0
                while curr in visitDict:
                    lenLeft += 1
                    visitDict[curr] = True
                    curr -= 1
                res = max(res, lenRight+lenLeft+1)
        return res    
"""