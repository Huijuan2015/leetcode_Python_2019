class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # mp = {}
        # for ch in s:
        #     if ch not in mp:
        #         mp[ch] = 1
        #     else:
        #         mp[ch] += 1

        mp = Counter(s)
        oddCounter = 0
 
        for value in mp.values():
            if value%2 == 1:
                oddCounter += 1
        if oddCounter > 1:
            return len(s) - oddCounter + 1
        return len(s)

