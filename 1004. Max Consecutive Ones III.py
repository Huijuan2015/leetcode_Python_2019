class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        i = 0
        for j in range(len(A)):
            # If we included a zero in the window we reduce the value of K.
            # Since K is the maximum zeros allowed in a window.
            K -= 1 - A[j]
            # A negative K denotes we have consumed all allowed flips and window has
            # more than allowed zeros, thus increment left pointer by 1 to keep the window size same.
            if K < 0:
                # If the left element to be thrown out is zero we increase K.
                K += 1 - A[i]
                i += 1
            print i, j ,K
        return j - i + 1
        # keep a K window, i ,j
        # keep a queue to store K 0 indexes
        # from collections import deque
        i, j = 0, 0
        q = deque()
        ans = -1
        # 扩展: q length < K+1
        # 缩小: i = q.popleft()+1
        while j < len(A):
            if len(q) < K+1:
                if A[j] == 0:
                    q.append(j)
                    if len(q) == K+1:
                        i = q.popleft()+1
            ans = max(ans, j-i+1)
            j += 1
        return ans      
        
        