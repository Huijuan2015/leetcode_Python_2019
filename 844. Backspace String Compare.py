class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        # 从后往前
        i, j = len(S)-1, len(T)-1
        skipS, skipT = 0, 0 
        while i >= 0 or j >= 0:
            while i >= 0:
                if S[i] == '#':
                    skipS += 1
                    i -= 1
                elif skipS>0:
                    skipS -= 1
                    i -=1
                else:
                    break
            while j >= 0:
                if T[j] == '#':
                    skipT += 1
                    j -= 1
                elif skipT>0:
                    skipT -= 1
                    j -=1
                else:
                    break
            if (i >= 0 and j >= 0 and S[i] != T[j]):
                return False
            # if (i < 0 and j >= 0) or (j < 0 and i >= 0) or :
            if ((i >= 0) != (j >= 0)):
                return False
            i -= 1
            j -= 1
        return True
        
        # stk1, stk2 = [], []
        # for ch in S:
        #     if ch != '#':
        #         stk1.append(ch)
        #     else:
        #         if stk1:
        #             stk1.pop()
        #         else:
        #             continue
        # for ch in T:
        #     if ch != '#':
        #         stk2.append(ch)
        #     else:
        #         if stk2:
        #             stk2.pop()
        #         else:
        #             continue
        # return stk1 == stk2