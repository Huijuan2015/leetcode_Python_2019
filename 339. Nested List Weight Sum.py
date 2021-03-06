class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        self.res = 0
        self.helper(nestedList, 1)
        return self.res
    
    def helper(self, nestedList, depth):
        newList = []
        for l in nestedList:
            if l.isInteger():
                self.res += l.getInteger()*depth
            else:
                self.helper(l.getList(), depth+1)

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


class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        return self.helper(nestedList, 1)
        
    def helper(self, nestedList, depth):
        cnt = 0
当前层， 如果是数字，就加入计算，如果不是数字，就继续递归， 并且层数+1，最后的结果中加入整个部分
        while nestedList:
            tmp = nestedList.pop()
            if tmp.isInteger():
                cnt += tmp.getInteger() * depth
            else:
                # guaranteed to return a list of some sort unless the default value provided is not a list.
                cnt += self.helper(tmp.getList(), depth+1)
        return cnt
    
        # depth, ans = 1, 0
        # while nestedList:
        #     ans += depth * sum( i.getInteger() for i in nestedList if i.isInteger())
        #     newList = []
        #     for i in nestedList:
        #         if not i.isInteger():
        #             newList += i.getList()
        #     nestedList = newList
        #     depth += 1
        # return ans