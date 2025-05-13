class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        mp_m = {}
        for ch in magazine:
            if ch not in mp_m:
                mp_m[ch] = 1
            else:
                mp_m[ch] += 1
        
        for ch in ransomNote:
            if ch in mp_m:
                mp_m[ch] -= 1
            if ch not in mp_m or mp_m[ch] < 0:
                return False
        return True


        # python:
        # magazine_count = Counter(magazine)