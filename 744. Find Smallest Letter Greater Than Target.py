class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if not letters:
            return
        # ans = ""
        # diff = float('inf')
        # 找到 letter 使得letter-target diff最小
        for l in letters:
            if l > target:
                return l
            # tmp = ord(l) - ord(target)
            # if tmp <= diff :
            #     ans = l
            #     diff = tmp
        return letters[0]
    
    二分法更快