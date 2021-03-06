# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
[[1,1],2,[1,1]]
用map来储存每一层sum，比如第一层[2] ,存1：2； 第二层 [1,1], [1,1] 存2：4
map: (
      1:2;
      2:2+2
      )

class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        from collections import defaultdict
        ans = 0
        self.mp = defaultdict(int) #用int 如果没有，默认返回0
        self.helper(nestedList, 1)
        depths = self.mp.keys()
        
        if not depths:
            return ans
        
        maxDepth = max(depths)  + 1
        for i in depths:
            ans += self.mp[i] * (maxDepth - i)
        return ans
    
    def helper(self, nestedList, depth):
        if not nestedList:
            return 0
        for list in nestedList:
            if list.isInteger():
                self.mp[depth] += list.getInteger()
            else:
                self.helper(list.getList(), depth + 1)

BFS
class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        total_sum, level_sum = 0, 0
        while len(nestedList):
            next_level_list = []
            for x in nestedList:
                if x.isInteger():
                    level_sum += x.getInteger()
                else:
                    for y in x.getList():
                        next_level_list.append(y)
            total_sum += level_sum
            nestedList = next_level_list
        return total_sum
            