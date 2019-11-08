class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        # stack 维持一个只递减的栈
        if not T:
            return []
        stk = []
        res = [0 for _ in range(len(T))]
        
        for i, t in enumerate(T):
            while stk and t > T[stk[-1]]:
                j = stk.pop()
                res[j] = i - j #计算天数即可
            stk.append(i)
        return res
            