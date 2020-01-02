class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # is palindrome permutation: char count is double
        # at most 1 extra char left
        from collections import defaultdict
        mp = defaultdict(int)
        
        for ch in s:
            mp[ch] += 1
        cnt = 0
        for ch_cnt in mp.values():
            if ch_cnt % 2 != 0:
                cnt += 1
                if cnt > 1:
                    return False
        return True