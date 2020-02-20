class Solution(object):
    def reconstructMatrix(self, upper, lower, colsum):
        """
        :type upper: int
        :type lower: int
        :type colsum: List[int]
        :rtype: List[List[int]]
        """
        m, n = 2, len(colsum)
        res = [[0 for _ in range(n)] for _ in range(m)]

            
        for j in range(n):
            if colsum[j] == 2:
                if upper and lower:
                    res[0][j], res[1][j] = 1, 1
                    upper -= 1
                    lower -= 1
                    colsum[j] = 0
                else:
                    return []
            elif colsum[j] == 1:
                if upper > lower:
                    res[0][j] = 1
                    upper -= 1
                else:
                    res[1][j] = 1
                    lower -= 1
            elif colsum[j] == 0:
                continue
            else:
                return []
        return res if not upper and not lower else []    

class Solution(object):
    def reconstructMatrix(self, upper, lower, colsum):
        """
        :type upper: int
        :type lower: int
        :type colsum: List[int]
        :rtype: List[List[int]]
        """
        m, n = 2, len(colsum)
        res = [[0 for _ in range(n)] for _ in range(m)]
        for j in range(n): #put 2 first
            if colsum[j] == 2:
                if upper and lower:
                    res[0][j], res[1][j] = 1, 1
                    upper -= 1
                    lower -= 1
                    colsum[j] = 0
                else:
                    return []
        for j in range(n):
            
            if colsum[j] == 1:
                if upper:
                    res[0][j] = 1
                    upper -= 1
                elif lower:
                    res[1][j] = 1
                    lower -= 1
                else:
                    return []
            elif colsum[j] == 0:
                continue
            else:
                return []
        return res if not upper and not lower else []    