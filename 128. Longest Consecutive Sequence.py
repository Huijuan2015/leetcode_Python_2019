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