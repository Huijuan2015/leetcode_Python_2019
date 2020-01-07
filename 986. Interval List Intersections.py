class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """

        i, j = 0, 0
        # A[i], B[j]
        res = []
        while i < len(A) and j < len(B):
            # tmp = [None, None]
            # 完全不重合
                #A比B小，i+1
                #B比A小，j+1
            a, b = A[i], B[j]
            if a[1] < b[0]:
                i += 1
            elif  b[1] < a[0]:
                j += 1
            # 有重合
            else:
                tmp = [max(a[0], b[0]), min(a[1], b[1])]   A,B  的阶段性可以保证 else不需要再考虑详细的大小
                res.append(tmp)
                if a[1] > b[1]:
                    j += 1
                else:
                    i += 1    
        return res
                
            
            