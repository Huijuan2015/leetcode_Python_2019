import re
class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        # sArray = re.sub( r"([A-Z])", r"\1", S).split('-')
        # # sArray = S.split('-')
        # string = ''
        # for ss in sArray:
        #     string += ss
        S = S.upper().replace('-','')
        size = len(S)
        cur = K if size%K == 0 else size%K
        res = S[:cur]
        while cur < size:
            res += '-' + S[cur:cur+K]
            cur += K
        return res
        
                    