class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        j = 0
        stk = []
        for x in pushed:
            stk.append(x)
            while stk and j < len(popped) and stk[-1] == popped[j]:
                stk.pop()
                j += 1
        return j == len(popped)
                

                