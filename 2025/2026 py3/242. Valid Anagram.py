class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
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
        


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s and not t:
            return True
        if not s or not t or len(s) != len(t):
            return False

        count_s = [0] * 26
        count_t = [0] * 26
        for i in range(len(s)):
            count_s[ord(s[i])- ord('a')] += 1
            count_t[ord(t[i])- ord('a')] += 1
        return count_s == count_t

1个数组
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s and not t:
            return True
        if not s or not t or len(s) != len(t):
            return False

        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i])- ord('a')] += 1
            count[ord(t[i])- ord('a')] -= 1
        return not any(count)
