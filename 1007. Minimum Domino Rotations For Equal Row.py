class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        # 如果能使得两行数字相同，那数字必须是A[0]或B[0]。
        # 所以依次对A[i]和B[i]查是否等于A[0]、B[0]。
        # 如果A[0]满足，就不需要查B[0]了，因为只有当A[0] == B[0]时才可能A和B都满足条件
        # 。‌数个数时不能数==A[0]或B[0]的，因为A和B可能存在相同元素
        # res, curr = float('inf'), 0
        def count(target, A, B):
            ans = 0
            for i in range(len(A)):
                if A[i] != target:
                    if B[i] == target:
                        ans += 1
                    else:
                        return float('inf')
            return ans
                    
        resA = min(count(A[0], A, B), count(A[0], B, A))
        resB = min(count(B[0], A, B), count(B[0], B, A))
        # print resA, resB
        res = float('inf')
        res = min(resA, resB)
        return res if res != float('inf') else -1
        

        

class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        from collections import defaultdict
        if len(A) != len(B):
            return -1
        mp = defaultdict(set)

        for idx, val in enumerate(A):
            mp[val].add(idx)
        # 从小的找
        res = len(A)+1
        for val, idxes in mp.items():
            # idxes not in idxes
            # print val, idxes
            curr = 0
            for i in range(len(A)):
                if i not in idxes:
                    if B[i] == val:
                        curr += 1
                    else:
                        break
            # print curr
            if curr+ len(idxes) == len(A):
                res = min(res, curr)
        
        mp2 = defaultdict(set)

        for idx, val in enumerate(B):
            mp2[val].add(idx)
        for val, idxes in mp2.items():
            # idxes not in idxes
            # print val, idxes
            curr = 0
            for i in range(len(B)):
                if i not in idxes:
                    if A[i] == val:
                        curr += 1
                    else:
                        break
            # print curr
            if curr+ len(idxes) == len(B):
                res = min(res, curr)
        return res if res != len(A)+1 else -1