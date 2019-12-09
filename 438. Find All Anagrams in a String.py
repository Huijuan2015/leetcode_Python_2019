class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # left, right cnt
        # move right: 
            #尽可能扩展right， right is valid, add to mp+1, cnt-1
            #扩展到符合条件cnt = 0: add left to res
            #扩展到大于条件：
                # move left
        if len(s) < len(p) or not s or not p:
            return []
        import collections
        mp = collections.Counter(p)
        cnt = len(p)
        res = []
        left, right = 0, 0 
        while right < len(s):
            if mp[s[right]] >= 1:
                cnt -= 1
            mp[s[right]] -= 1 
            right += 1
            if cnt == 0:
                res.append(left)
            if right - left == len(p):
                if mp[s[left]] >= 0:
                      cnt += 1
                mp[s[left]] += 1
                left += 1
        return res
                
            
https://blog.csdn.net/yy254117440/article/details/53025142