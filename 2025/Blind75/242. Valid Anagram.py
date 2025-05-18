class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        count_s = [0] * 26
        count_t = [0] * 26

        for i in range(len(s)):
            count_s[ord(s[i]) - ord('a')] += 1
            count_t[ord(t[i]) - ord('a')] += 1
        return count_s == count_t


        
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s and not t:
            return True
        if not s or not t or len(s) != len(t):
            return False
        mp = collections.Counter(s)
        for i in range(len(t)):
            if t[i] in mp:
                mp[t[i]] -= 1
            if t[i] not in mp or mp[t[i]] < 0:
                return False
        return True

            
